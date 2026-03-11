class BeliefEdge:
    def __init__(self, source, target, weight=0.5, relationship="support"):
        self.source = source
        self.target = target
        self.weight = weight
        self.relationship = relationship

    def propagate(self):
        change = self.source.confidence - self.target.confidence
        adjustment = self.weight * change

        if self.relationship == "support":
            self.target.confidence += adjustment

        elif self.relationship == "contradict":
            self.target.confidence -= adjustment

        if self.target.confidence > 1:
            self.target.confidence = 1

        if self.target.confidence < 0:
            self.target.confidence = 0

        return self.target.confidence
