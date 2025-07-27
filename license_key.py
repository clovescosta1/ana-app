from app import db
from datetime import datetime, timedelta
import enum

class LicenseKeyStatus(enum.Enum):
    AVAILABLE = "AVAILABLE"
    ACTIVE = "ACTIVE"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"

class LicenseKey(db.Model):
    __tablename__ = "license_key"

    id = db.Column(db.Integer, primary_key=True)
    key_string = db.Column(db.String(80), unique=True, nullable=False)
    validity_period_days = db.Column(db.Integer, nullable=False, default=30)  # Default to 30 days
    status = db.Column(db.Enum(LicenseKeyStatus), nullable=False, default=LicenseKeyStatus.AVAILABLE)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=True)
    user = db.relationship("User", backref=db.backref("license_keys", lazy=True))
    
    activated_at = db.Column(db.DateTime, nullable=True)
    expires_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<LicenseKey {self.key_string} ({self.status.value})>"

    def activate(self, user):
        if self.status == LicenseKeyStatus.AVAILABLE:
            self.user_id = user.id
            self.status = LicenseKeyStatus.ACTIVE
            self.activated_at = datetime.utcnow()
            if self.validity_period_days > 0: # 0 or negative could mean indefinite/lifetime
                self.expires_at = self.activated_at + timedelta(days=self.validity_period_days)
            else:
                self.expires_at = None # Or a very far future date for lifetime keys
            db.session.commit()
            return True
        return False

    def revoke(self):
        self.status = LicenseKeyStatus.REVOKED
        db.session.commit()

    def check_if_expired(self):
        if self.status == LicenseKeyStatus.ACTIVE and self.expires_at and self.expires_at < datetime.utcnow():
            self.status = LicenseKeyStatus.EXPIRED
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_active_key_for_user(user_id):
        key = LicenseKey.query.filter_by(user_id=user_id, status=LicenseKeyStatus.ACTIVE).first()
        if key and key.check_if_expired():
            return None # Key was active but just expired
        return key
