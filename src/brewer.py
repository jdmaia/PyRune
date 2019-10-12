class Brewer:
    runes = ''
    brewerName = ''
    totalMana  = 0
    logger     = ''

    def __init__(self, name, totalManaCost, logger):
        self.name     = name
        self.totaMana = totalManaCost
        print("Starting brewer for " + self.name + " TOTALMANA: " + str(self.totalMana))
        print("Recording output file to " + self.name + ".log")
        self.logger = logger
    def AttachRune(self, rune):
        # does append do a copy? How does memory management works here?
        self.runes.append(rune)

    def StartBrews(self):
        for x in runes:
            x.Brew(self.logger)
        return

    def StopBrews(self):
        for x in runes:
            x.Abort()
        return

    # Alright, I think thats it :)
