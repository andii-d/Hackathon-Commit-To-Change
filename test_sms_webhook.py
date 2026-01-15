from app import app


def test_sms_webhook_reply():
    client = app.test_client()
    response = client.post(
        "/sms",
        data={"Body": "I walked 10k steps", "From": "+15551234567"},
    )
    assert response.status_code == 200
    body = response.get_data(as_text=True)
    assert "Got it: I walked 10k steps." in body
