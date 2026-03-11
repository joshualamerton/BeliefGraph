from core.belief_graph import Belief
from core.propagation_engine import BeliefEdge

# belief A
interest_rates = Belief(
    belief_id="interest_rates_increase",
    statement="Interest rates are increasing",
    confidence=0.6
)

# belief B
housing_affordability = Belief(
    belief_id="affordability_declines",
    statement="Housing affordability declines when interest rates rise",
    confidence=0.5
)

# belief C
housing_demand = Belief(
    belief_id="housing_demand_strong",
    statement="Housing demand remains strong",
    confidence=0.7
)

print("Initial beliefs")
print("Interest rates:", interest_rates.confidence)
print("Affordability:", housing_affordability.confidence)
print("Housing demand:", housing_demand.confidence)

# update interest rate belief
interest_rates.add_evidence(0.85)
interest_rates.update_confidence()

print("\nAfter evidence update")
print("Interest rates:", interest_rates.confidence)

# support relationship
support_edge = BeliefEdge(
    source=interest_rates,
    target=housing_affordability,
    weight=0.7,
    relationship="support"
)

# contradiction relationship
contradiction_edge = BeliefEdge(
    source=interest_rates,
    target=housing_demand,
    weight=0.6,
    relationship="contradict"
)

support_edge.propagate()
contradiction_edge.propagate()

print("\nAfter propagation")
print("Affordability:", housing_affordability.confidence)
print("Housing demand:", housing_demand.confidence)
