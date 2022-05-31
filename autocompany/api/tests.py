from rest_framework import status
from rest_framework.test import APITestCase

from autocompany.api.models import Client, Order


class AddCartToOrder(APITestCase):

    def setUp(self) -> None:
        self.client = Client.objects.create(
            customer_code="001TST",
            first_name="TST",
            last_name="TST",
            pref_name="TST",
            gender="M",
            mobile_number="TST",
            email="abc@abc.com",
        ),
        self.order = Order.objects.create(
            order_number="001",
            client=self.client.id,
            address="Test",
            delivery_date="2022-09-09T15:58:00Z",
            delivery_fee=""
        ),


    def test_current_without_translation_file(self):
        url = f"/api/v1/order/items/cart/add/{self.order.order_number}"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # self.assertEqual(
        #     response.data.get("id"), self.self.order.id
        # )
