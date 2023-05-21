from fastapi import APIRouter, Depends, BackgroundTasks
from tasks.tasks import send_email_report_dashboard
from auth.auth import current_user

router = APIRouter(
    prefix="/report"
)


@router.get("/dashboard")
def get_dashboard_report(user=Depends(current_user)):
    send_email_report_dashboard.delay(user.username)
    return {
        "status": 200,
        "data": "Письмо отправлено",
        "details": None
    }