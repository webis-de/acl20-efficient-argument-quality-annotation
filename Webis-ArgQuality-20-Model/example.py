from bradleyterry import BradleyTerry

# Comparisons are given in the form of (ID_A, ID_B, Tie)
# The order of IDs denotes the direction of the comparison. If Tie is True, the order is ignored.
# The input format can be customized by supplying a custom parsing function to the model
comparisons = [
        ('A','B',False),
        ('A','C',False),
        ('A','D',False),
        ('B','C',True),
        ('B','D',False),
        ('C','B',False),
        ('C','D',False),
        ('D','A',False),
    ]

# Initialize the model with given comparisons
bt = BradleyTerry(comparisons)

# Fit the model using supplied hyperparameters
bt.fit(regularization = 0.3, threshold = 0.01)

# Get the calculated merits
print(bt.get_merits())
#>>> [('D', 0.32692689118596696), ('B', 0.7570454645168428), ('C', 1.2429546060392827), ('A', 1.673073287350478)]

# Merits can be normalized to the 0-1 range
print(bt.get_merits(normalize=True))
#>>> [('D', 0.0), ('B', 0.3195185203522548), ('C', 0.680481543344691), ('A', 1.0)]
