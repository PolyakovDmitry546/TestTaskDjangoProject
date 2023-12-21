const stripe_public_key = JSON.parse(document.getElementById('stripe-public-key').textContent);
stripe = Stripe(stripe_public_key)
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