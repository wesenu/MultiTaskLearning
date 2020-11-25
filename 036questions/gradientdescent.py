

#if f(theta) = ({c1:.2f}*theta+{c2:.2f}) squared and theta = {theta_a:.2f} what is f(theta) ?

#can try this with just all of the positions? havent yet
    # quant_cell_positions = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 23, 24, 25, 26, 27, 28, 29, 30]
def return_data(train_id, test_id):
    count = 0
    train_data = []
    test_data = []
    test_answers = []
    for theta in [1, 4, 6, 9.4, 3, 15.4, 0.5, 0.23]:
        for c1 in [3, 4, 7, 10, 0.3]:
            for c2 in [19, 3, 5, 6, 8]:
                answer = (c1*theta+c2)*(c1*theta+c2)
                #make sure there are no spaces in the formula
                formula = "({c1:.2f}*{theta:.2f}+{c2:.2f})*({c1:.2f}*{theta:.2f}+{c2:.2f})"
                formula = formula.format(c1 = c1, c2 = c2, theta = theta)
                question = "if f(theta) equals {c1:.2f} times theta plus {c2:.2f} squared and theta = {theta:.2f} what is f(theta) ?"
                question = question.format(c1 = c1, c2 = c2, theta = theta)
                quant_cell_positions = get_quant_cells(question)

                if count % 3 != 0:
                    train_dict = {"expression": formula, "quant_cell_positions": quant_cell_positions, "processed_question": question, "raw_question": question, "is_quadratic": False, "Id": train_id, "Expected": answer}
                    train_data.append(train_dict)
                    train_id += 1
                else:
                    test_dict = {"quant_cell_positions": quant_cell_positions, "processed_question": question, "raw_question": question, "is_quadratic": False, "Id": test_id}
                    test_data.append(test_dict)
                    answer_dict = {"Id": test_id, "answer": answer}
                    test_answers.append(answer_dict)
                    test_id += 1
                count += 1
    return train_data, test_data, test_answers

def get_quant_cells(question):
    return [i for i in range(len(question.split(" ")))]