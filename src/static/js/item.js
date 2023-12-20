stripe = Stripe('pk_test_51OPNm2Ahth7NeWYb2fIJvnsPt03uD6TVcIlCYY9shN0mVyOkSpJpzxS64YWCfuOZTHpeU4wDsFD56yHU2U6EIhkq00UrzBATU7')
const buy_button = document.getElementById("buy-button");

function getStripeSessionId() {
    const buy_url = document.getElementById("buy-url").textContent;
    fetch(buy_url, {
        method: 'GET',
      })
      .then(function(response) {
        return response.json();
      })
      .then(function(session) {
        return stripe.redirectToCheckout({ sessionId: session.session_id });
      })
      .then(function(result) {
        if (result.error) {
          alert(result.error.message);
        }
      });
}

buy_button.addEventListener('click', getStripeSessionId);