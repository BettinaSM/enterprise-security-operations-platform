from parsers.threat_feed import (
    load_threat_feed,
    correlate_threat_feed
)

from parsers.threat_intelligence import (
    enrich_iocs
)

def process_threat_intelligence(
    ioc_matches,
    path
):

    feed = load_threat_feed(path)

    correlations = correlate_threat_feed(
        ioc_matches,
        feed
    )

    enrichment = enrich_iocs(
        ioc_matches
    )

    return {
        "feed": feed,
        "correlations": correlations,
        "enrichment": enrichment
    }
