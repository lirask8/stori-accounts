from django.template.loader import render_to_string
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import AllowAny
from common.process_file import ProcessFile
from common.utils import CommonMixin
from transactions.models import Account, Transaction


class ProcessFileAPIView(APIView, CommonMixin):
    # Allow any for testing
    permission_classes = (AllowAny,)

    def post(self, request):

        account_id = request.data.get("account_id")
        if not account_id:
            return Response({"message": "Missing account id"}, status.HTTP_400_BAD_REQUEST)
        account = self.get_object_or_none(Account, id=account_id)
        if not account:
            return Response({"message": "Unknown account id"}, status.HTTP_400_BAD_REQUEST)

        try:
            file_data = request.data["file"]
            file_processor = ProcessFile(file_data)
            file_transactions = file_processor.process_rows()
            transactions = []
            for row in file_transactions:
                transactions.append(
                    Transaction(
                        account_id=account_id,
                        id_in_file=row["id"],
                        date=row["date"],
                        amount=row["amount"],
                        is_credit=row["is_credit"],
                    )
                )

            Transaction.objects.bulk_create(transactions)
            # Transaction.objects.filter(account=account, is_credit=False).aggregate(Sum("amount"))
            summary = file_processor.get_summary_data()
            summary["account_id"] = account_id

            html_mail = render_to_string('email/summary.html', summary)

            sendmail = self.send_email(
                subject="Transactions summary",
                html_content=html_mail,
                sender="no-reply@support.com",
                to=["backoffice@mail.com"]
            )

        except MultiValueDictKeyError:
            return Response(
                {"message": "Missing file to process"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response({"Summary": summary}, status.HTTP_200_OK)
