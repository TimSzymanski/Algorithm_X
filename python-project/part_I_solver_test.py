from part_I_generate_solutions import main_program
from timinator import CONGRATS
import random

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

# def test_03_generate_solutions():
#     try:
#         count1 = count_all_stars([2, 3])
#         assert count1 == 5, "Running count_all_stars([2, 3])... Expected 5, got {}".format(count1)
#         count2 = count_all_stars([9, -3])
#         assert count2 == 6, "Running count_all_stars([9, -3])... Expected 6, got {}".format(count2)
#         success()

#         if sum_builtin_used:
#             send_msg("My personal Yoda, you are. 🙏", "* ● ¸ .　¸. :° ☾ ° 　¸. ● ¸ .　　¸.　:. • ")
#             send_msg("My personal Yoda, you are. 🙏", "           　★ °  ☆ ¸. ¸ 　★　 :.　 .   ")
#             send_msg("My personal Yoda, you are. 🙏", "__.-._     ° . .　　　　.　☾ ° 　. *   ¸ .")
#             send_msg("My personal Yoda, you are. 🙏", "'-._\\7'      .　　° ☾  ° 　¸.☆  ● .　　　")
#             send_msg("My personal Yoda, you are. 🙏", " /'.-c    　   * ●  ¸.　　°     ° 　¸.    ")
#             send_msg("My personal Yoda, you are. 🙏", " |  /T      　　°     ° 　¸.     ¸ .　　  ")
#             send_msg("My personal Yoda, you are. 🙏", "_)_/LI")
#         else:
#             send_msg("Kudos 🌟", "Did you know that you could use the sum function? Try it!")
#             send_msg("Kudos 🌟", "")
#             send_msg("Kudos 🌟", "galaxies = [37, 3, 2]")
#             send_msg("Kudos 🌟", "total_stars = sum(galaxies)  # 42")

#             solver = MySolver()
#             for solution in solver.solve():
#                 for action in solution:
#                     send_msg("Solver Steps", f'{action}')
                    
#     except AssertionError as e:
#         fail()
#         send_msg("Oops! 🐞", e)
#         send_msg("Hint 💡", "Did you properly accumulate all stars into 'total_stars'? 🤔")


if __name__ == "__main__":
    main_program()
    success()
    send_msg(f"{random.choice(CONGRATS)} 🌟", "Hopefully the actions printed!")
