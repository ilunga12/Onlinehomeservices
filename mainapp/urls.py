from django.urls import path

from mainapp import views, adminviews, workerviews, customerviews

urlpatterns = [
    path("",views.land,name="land"),
    path("login_view",views.login_view,name="login_view"),








    ###################admin###############
    path("admin1",adminviews.admin1,name="admin1"),
    path("adminbase",adminviews.adminbase,name="adminbase"),
    path("work_view",adminviews.work_view,name="work_view"),
    path("delete/<int:id>/",adminviews.delete,name="delete"),
    path("worke_add", adminviews.worke_add, name="worke_add"),
    path("ViewWorker",adminviews.ViewWorker,name="ViewWorker"),
    path("deleteW/<int:id>/",adminviews.deleteW,name="deleteW"),
    path("ViewCustomer",adminviews.ViewCustomer,name="ViewCustomer"),
    path("deleteC/<int:id>/", adminviews.deleteC, name="deleteC"),
    path("ViewWorkerschedule",adminviews.ViewWorkerschedule,name="ViewWorkerschedule"),
    path("ViewcustomerFeedback",adminviews.ViewcustomerFeedback,name="ViewcustomerFeedback"),
    path("CustomerFeedbackReply/<int:id>/",adminviews.CustomerFeedbackReply,name="CustomerFeedbackReply"),
    path("NotificationAdd",adminviews.NotificationAdd,name="NotificationAdd"),
    path("notificationiew_admin",adminviews.notificationiew_admin,name="notificationiew_admin"),
    path("deletenot/<int:id>/",adminviews.deletenot,name="deletenot"),
    path("booking_status",adminviews.booking_status,name="booking_status"),
    path("status_approve/<int:id>/",adminviews.status_approve,name="status_approve"),
    path("status_reject/<int:id>/",adminviews.status_reject,name="status_reject"),
    path("Bill_Payments",adminviews.Bill_Payments,name="Bill_Payments"),
    path("payment_status",adminviews.payment_status,name="payment_status"),





#############################worker###########33333333
    path("workerbase",workerviews.workerbase,name="workerbase"),
    path("regworkrbase",workerviews.regworkrbase,name="regworkrbase"),
    path("regworkr",workerviews.regworkr,name="regworkr"),
    path("regupdate/<int:id>/",workerviews.regupdate,name="regupdate"),
    path("ScheduleAdd",workerviews.ScheduleAdd,name="ScheduleAdd"),
    path("ScheduleView",workerviews.ScheduleView,name="ScheduleView"),
    path("ScheduleUpdate/<int:id>/", workerviews.ScheduleUpdate, name="ScheduleUpdate"),
    path("deleteSchedule/<int:id>/", workerviews.deleteSchedule, name="deleteSchedule"),
    path("NotificationView",workerviews.NotificationView,name="NotificationView"),







#############customer#######
    path("customerbase",customerviews.customerbase,name="customerbase"),
    path("customerbasereg",customerviews.customerbasereg,name="customerbasereg"),
    path("reguser",customerviews.reguser,name="reguser"),
    path("customer_feedback",customerviews.customer_feedback,name="customer_feedback"),
    path("feedback_view",customerviews.feedback_view,name="feedback_view"),
    path("notification_viewcust",customerviews.notification_viewcust,name="notification_viewcust"),
    path("scheduleviewcust",customerviews.scheduleviewcust,name="scheduleviewcust"),
    path("schedulebook/<int:id>/",customerviews.schedulebook,name="schedulebook"),
    path("appointment_status",customerviews.appointment_status,name="appointment_status"),
    path("payment_view",customerviews.payment_view,name="payment_view"),
    path("cardpayment/<int:id>/",customerviews.cardpayment,name="cardpayment"),
    path("direct_payment/<int:id>/",customerviews.direct_payment,name="direct_payment"),
]