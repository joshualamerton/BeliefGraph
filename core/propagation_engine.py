class BeliefEdge:
    def __init__(self, source, target, weight=0.5):
        self.source = source
        self.target = target
        self.weight = weight

    def propagate(self):
        change = self.source.confidence - self.target.confidence
        adjustment = self.weight * change
        self.target.confidence += adjustment

        if self.target.confidence > 1:
            self.target.confidence = 1
        if self.target.confidence < 0:
            self.target.confidence = 0

        return self.target.confidence
