from django.urls import path
from .views import (index, my_tests, create_test, create_question, update_test, detail_test,
                     update_question, ready_to_test, test, check_test, my_results )

urlpatterns = [
    path("", index, name="index"),
    path("my_tests/", my_tests, name="my_tests"),
    path("my_results/", my_results, name="my_results"),
    path("create_test/", create_test, name="create_test"),
    path("create_question/<int:test_id>/", create_question, name="create_question"),
    path("update_test/<int:test_id>/", update_test, name="update_test"),
    path("detail_test/<int:test_id>/", detail_test, name="detail_test"),
    path("update_question/<int:question_id>/", update_question, name="update_question"),
    path("ready_to_test/<int:test_id>/", ready_to_test, name="ready_to_test"),
    path("test/<int:test_id>/", test, name="test"),
    path("check_test/<int:checktest_id>/", check_test, name="check_test"),
]
