# privizor
A library for apply mathematically rigorous "jittering" to data in order to counteract the database reconstruction theorem.

## Usage
**data = privizor(data, epsilon, chunks = 10000, options = {}, data_keys = [], str_change = 0.25)**

`data`: a list of dictionaries and/or lists
`epsilon`: the percentage of accuracy to lose (given as a number between 0 and 1)
`chunks`: the amount of chunks for the jitterer to pseudo-randomly distribute
`options`: a dict in the form of `'data_label': [ 'option1', 'option2', 'option3' ],`
`data_keys`: a way to specify `data_label`s when not using a list of dictionaries
`str_change`: the threshhold that a non-number value has to hit before it changes to a randomly selected value from the options dict
