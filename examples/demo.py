from core.belief_graph import Belief

# create a belief
belief = Belief(
    belief_id="mortgage_affordability",
    statement="Higher interest rates reduce home affordability",
    confidence=0.6
)

print("Initial confidence:", belief.confidence)

# add new evidence
belief.add_evidence(likelihood=0.85)

# update belief
new_confidence = belief.update_confidence()

print("Updated confidence:", new_confidence)
