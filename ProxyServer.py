from mitmproxy import http
import random

# Liste de faux user agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:90.0) Gecko/20100101 Firefox/90.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
    # Ajouter d'autres user agents si nécessaire
]

# Liste de domaines de trackers à bloquer
TRACKER_DOMAINS = ["google-analytics.com", "hubspot.com", "mixpanel.com", "matomo.org", "tealium.com", "segment.com", "quantserve.com"]

def get_random_user_agent():
    return random.choice(USER_AGENTS)

def request(flow: http.HTTPFlow) -> None:
    hostname = flow.request.pretty_url

    # Bloquer les domaines des trackers
    if any(tracker in hostname for tracker in TRACKER_DOMAINS):
        flow.response = http.Response.make(
            403,  # Status code
            b"Access denied",  # Response body
            {"Content-Type": "text/plain"}  # Headers
        )
        return

    # Modifier les en-têtes de la requête pour réduire le fingerprinting
    flow.request.headers["User-Agent"] = get_random_user_agent()
    flow.request.headers.pop("Accept-Language", None)
    flow.request.headers.pop("Accept-Encoding", None)
    flow.request.headers.pop("Connection", None)
    flow.request.headers.pop("Upgrade-Insecure-Requests", None)
    flow.request.headers.pop("TE", None)

    # Bloquer les requêtes pour les tracking pixels
    if flow.request.pretty_url.endswith((".png", ".jpg", ".jpeg", ".gif", ".webp")) and flow.request.headers.get("Referer"):
        referer = flow.request.headers.get("Referer")
        if any(tracker in referer for tracker in TRACKER_DOMAINS):
            flow.response = http.Response.make(
                403,  # Status code
                b"Access denied",  # Response body
                {"Content-Type": "text/plain"}  # Headers
            )
            return

