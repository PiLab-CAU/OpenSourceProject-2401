def get_true_answer(answer, feedback):
        if answer=='positive' and feedback is True:
            return 'positive'
        elif answer=='positive' and feedback is False:
            return 'negative'
        elif answer=='negative' and feedback is True:
            return 'negative'
        elif answer=='negative' and feedback is False:
            return 'positive'
        else:
            return 'negative'
