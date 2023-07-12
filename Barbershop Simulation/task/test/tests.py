from hstest import StageTest, CheckResult, dynamic_test, TestedProgram


class BarbershopSimulation(StageTest):

    @staticmethod
    def check_answer_length(user_output_length, correct_answer_length):
        if not user_output_length:
            return CheckResult.wrong('Your program did not print any results.')
        elif user_output_length < correct_answer_length:
            return CheckResult.wrong(f'Your program should print {correct_answer_length} lines '
                                     f'but {user_output_length} line(s) were found in the output.\n'
                                     f'You should print the 95% quantile of the maximum waiting time, '
                                     f'the average closing time delay, '
                                     f'the probability that maximum number of visitors in line is greater that 5.')
        else:
            return CheckResult.wrong(f'Your program printed more lines than expected: '
                                     f'there should be {correct_answer_length} lines '
                                     f'but {user_output_length} were found in the output.\n'
                                     f'You should print the 95% quantile of the maximum waiting time, '
                                     f'the average closing time delay, '
                                     f'the probability that maximum number of visitors in line is greater that 5.')

    @staticmethod
    def check_answer_values(user_output, correct_output):
        for output_line, correct_line in zip(user_output, correct_output):
            output_line = list(map(float, output_line.split()))
            if len(output_line) != 1:
                return CheckResult.wrong('Each line in the output should contain only 1 number.')
        if abs(float(user_output[0]) - correct_output[0]) > 8:
            return CheckResult.wrong('Incorrect 95% quantile of the maximum waiting time.')
        elif abs(float(user_output[1]) != correct_output[1]) > 1:
            return CheckResult.wrong('Incorrect average closing time delay.')
        elif abs(float(user_output[2]) != correct_output[2]) > 1:
            return CheckResult.wrong('Incorrect probability that maximum number of visitors in line is greater that 5.')
        return CheckResult.correct()

    @dynamic_test
    def test1(self):
        main = TestedProgram()
        main.start()
        output = main.execute('40 20 60 3').splitlines()
        correct_output = [34.32429698564698, 4.733889516656486, 0.00369]

        while '' in output:
            output.remove('')
        if len(output) != len(correct_output):
            return self.check_answer_length(len(output), len(correct_output))
        return self.check_answer_values(output, correct_output)

    @dynamic_test
    def test2(self):
        main = TestedProgram()
        main.start()
        output = main.execute('25 20 50 2').splitlines()
        correct_output = [340.86530299192, 181.45820136637525, 0.5393100000000001]

        while '' in output:
            output.remove('')
        if len(output) != len(correct_output):
            return self.check_answer_length(len(output), len(correct_output))
        return self.check_answer_values(output, correct_output)

    @dynamic_test
    def test3(self):
        main = TestedProgram()
        main.start()
        output = main.execute('20 20 50 4').splitlines()
        correct_output = [15.981632932440839, 1.6875411716384328, 0.00272]

        while '' in output:
            output.remove('')
        if len(output) != len(correct_output):
            return self.check_answer_length(len(output), len(correct_output))
        return self.check_answer_values(output, correct_output)


if __name__ == '__main__':
    BarbershopSimulation().run_tests()