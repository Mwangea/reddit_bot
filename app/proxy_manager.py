from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models import Proxy
from datetime import datetime

def get_next_proxy(session: Session) -> Proxy:
    return session.query(Proxy).filter(Proxy.is_active == True).order_by(func.coalesce(Proxy.last_used, datetime.min)).first()

def update_proxy_usage(session: Session, proxy: Proxy):
    proxy.last_used = datetime.utcnow()
    session.commit()

def get_proxy_dict(proxy: Proxy) -> dict:
    return {
        f"{proxy.protocol}": f"{proxy.protocol}://{proxy.address}:{proxy.port}"
    }