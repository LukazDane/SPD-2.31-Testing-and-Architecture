# by Kami Bigdely
# Rename Method
# Reference: https://parade.com/1039985/marynliles/pick-up-lines/

# TODO: Rename this function to reflect what it's doing.
def cal_un_gr(graph):
    """Calculate the area under the input graph."""
    # bla bla bla.
    pass

#####################


def get_max(li):  # TODO: Rename this function to reflect what it's doing.
    m = li[0]
    for value in li:
        if value > m:
            m = value
    return m


li = [5, -1, 43, 32, 87, -100]
print(get_max(li))

############################


# TODO: Rename this function to reflect what it's doing.
def sentence_splitter(sentence):
    words = sentence[0:].split(' ')
    return words


print(sentence_splitter('If you were a vegetable, you’d be a ‘cute-cumber.'))
