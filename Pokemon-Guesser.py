import openpyxl as xl
import statistics

wb = xl.load_workbook("Pokemon Database.xlsx")                 # Lowered priority values for Q20, Q22, Q25, QX2, QX4
sheet = wb["Sheet1"]

play = True                                                    # Can eliminate the issue with repeating remaining
                                                               # pokemon number by moving the code below each
                                                               # question (Could have a toggle on/off) 
while play:
    current_question = 0

    evolves = False
    evolved = False
    first_stage = False
    dual_type = False
    no_dual_type = False
    dual_type_evo = False
    no_dual_type_evo = False
    starter = False
    breed = False
    non_breed = False
    legend = False
    non_legend = False
    branched = False
    cross_g = False
    regional = False
    evo_regional = False
    mega = False
    non_mega = False
    gmax = False
    gmax_evo = False
    pre_gmax = False
    multi_head = False
    levelup = False
    no_levelup = False
    wings = False
    no_wings = False
    floating = False
    no_floating = False
    legs = False
    no_legs = False
    baby = False
    foss = False
    tail = False
    no_tail = False
    evo_tail = False
    no_evo_tail = False
    horn = False
    no_horn = False
    male_only = False
    female_only = False
    genderless = False
    mixed_gender = False
    ask_male = False
    ask_female = False
    ask_genderless = False
    same_type1 = False
    same_type2 = False
    color_type1 = False
    color_type2 = False
    same_color1 = False
    gloves = False
    any_move = False
    bear = False
    color_change = False
    third_evo = False
    not_third_evo = False
    minus_cheeks = False
    pre_evo_type = False
    no_pre_evo_type = False
    evo_type_change = False
    no_evo_type_change = False

    enter_question_decider = True
    skip = 0
    next_type = 1
    qcount = 1
    gl = guesslist = []
    sc = sheet.cell
    yes_no = []
    typ = types = []
    dex_color = []
    importance_ratingx = 0
    pnum = 695  # Total number of Pokemon +1
    next_question = 0

    true_false4b = True
    true_false5 = True
    true_false6 = True
    true_false7 = True
    true_false8 = True
    true_false8b = True
    true_false9 = True
    true_false9b = True
    true_false10 = True
    true_false11 = True
    true_false12 = True
    true_false12b = True
    true_false13 = True
    true_false14 = True
    true_false15 = True
    true_false16 = True
    true_false17 = True
    true_false18 = True
    true_false19 = True
    true_false20 = True
    true_false21 = True
    true_false21b = True
    true_false22 = True
    true_false23 = True
    true_false24 = True
    true_false24b = True
    true_false25 = True
    true_false26 = True
    true_false27 = True
    true_false28 = True
    true_false29 = True
    true_false30 = True
    true_false31 = True
    true_false32 = True
    true_false33 = True
    true_false34 = True
    true_false35 = True


    def gender():
        global male_only
        global female_only
        global mixed_gender
        global genderless
        global ask_male
        global ask_female
        global ask_genderless
        global n
        for n in range(2, pnum):
            if sc(n, 1).value in gl:
                if sc(n, 31).value == "Yes":
                    if sc(n, 32).value == "Yes":
                        mixed_gender = True
                    if sc(n, 32).value == "No":
                        male_only = True
                if sc(n, 31).value == "No":
                    if sc(n, 32).value == "Yes":
                        female_only = True
                    if sc(n, 32).value == "No":
                        genderless = True

        if male_only:
            if female_only:
                if mixed_gender:
                    if genderless:
                        ask_male = True  # Everything
                        ask_female = True
                    if not genderless:
                        ask_male = True  # Everything but Genderless
                        ask_female = True
                if not mixed_gender:
                    if genderless:
                        ask_male = True  # Everything but Mixed gender
                        ask_female = True
                    if not genderless:
                        ask_male = True  # Male only / Female only
            if not female_only:
                if mixed_gender:
                    if genderless:
                        ask_female = True  # Everything but Female only
                        ask_genderless = True
                    if not genderless:
                        ask_female = True  # Male only / Mixed gender
                if not mixed_gender:
                    if genderless:
                        ask_genderless = True  # Male only / Genderless
                    if not genderless:
                        pass  # Male only
        if not male_only:
            if female_only:
                if mixed_gender:
                    if genderless:
                        ask_male = True  # Everything but Male only
                        ask_genderless = True
                    if not genderless:
                        ask_male = True  # Female only / Mixed gender
                if not mixed_gender:
                    if genderless:
                        ask_genderless = True  # Female only / Genderless
                    if not genderless:
                        pass  # Female only
            if not female_only:
                if mixed_gender:
                    if genderless:
                        ask_genderless = True  # Mixed gender / Genderless
                    if not genderless:
                        pass  # Mixed gender only
                if not mixed_gender:
                    if genderless:
                        pass  # Genderless only
                    if not genderless:
                        pass  # Nothing


    for n in range(2, pnum):
        gl.append(sc(n, 1).value)

    print("Welcome to my Pokemon guessing game, please think of a Pokemon.")
    answer1 = input("QUESTION " + str(qcount) + ": Is your Pokemon from one of the following: Kanto, Johto, Hoenn or "
                                                "Sinnoh? ")
    qcount += 1
    print("Remaining Pokemon = " + str(len(gl)))
    if answer1 == "yes":
        for n in range(2, pnum):
            if sc(n, 7).value != "Kanto":
                if sc(n, 7).value != "Johto":
                    if sc(n, 7).value != "Hoenn":
                        if sc(n, 7).value != "Sinnoh":
                            gl.remove(sc(n, 1).value)
    elif answer1 == "no":
        for n in range(2, pnum):
            if sc(n, 7).value == "Kanto":
                gl.remove(sc(n, 1).value)
            elif sc(n, 7).value == "Johto":
                gl.remove(sc(n, 1).value)
            elif sc(n, 7).value == "Hoenn":
                gl.remove(sc(n, 1).value)
            elif sc(n, 7).value == "Sinnoh":
                gl.remove(sc(n, 1).value)

        answer1b = input("QUESTION " + str(qcount) + ": Is your Pokemon from Galar? ")
        qcount += 1
        print("Remaining Pokemon = " + str(len(gl)))
        if answer1b == "yes":
            for n in range(2, pnum):
                if sc(n, 7).value != "Galar" and sc(n, 1).value in gl:
                    gl.remove(sc(n, 1).value)
        elif answer1b == "no":
            for n in range(2, pnum):
                if sc(n, 7).value == "Galar" and sc(n, 1).value in gl:
                    gl.remove(sc(n, 1).value)

    answer2 = input("QUESTION " + str(qcount) + ": Does your Pokemon evolve? ")
    qcount += 1
    print("Remaining Pokemon = " + str(len(gl)))
    if answer2 == "yes":
        for n in range(2, pnum):
            if sc(n, 5).value != "Yes" and sc(n, 1).value in gl:
                gl.remove(sc(n, 1).value)
                evolves = True
    elif answer2 == "no":
        for n in range(2, pnum):
            if sc(n, 5).value != "No" and sc(n, 1).value in gl:
                gl.remove(sc(n, 1).value)

    answer3 = input("QUESTION " + str(qcount) + ": Does it evolve from something? ")
    qcount += 1
    print("Remaining Pokemon = " + str(len(gl)))
    if answer3 == "yes":
        for n in range(2, pnum):
            if sc(n, 6).value == "No" and sc(n, 1).value in gl:
                gl.remove(sc(n, 1).value)
                evolved = True
    elif answer3 == "no":
        for n in range(2, pnum):
            if sc(n, 6).value == "Yes" and sc(n, 1).value in gl:
                gl.remove(sc(n, 1).value)
                first_stage = True

    if evolves:
        if first_stage:
            answer2b = input("QUESTION " + str(qcount) + ": Can your Pokemon only evolve once? ")
            qcount += 1
            print("Remaining Pokemon = " + str(len(gl)))
            if answer2b == "yes":
                for n in range(2, pnum):
                    if sc(n, 25).value == "No" and sc(n, 1).value in gl:
                        gl.remove(sc(n, 1).value)
            elif answer2b == "no":
                for n in range(2, pnum):
                    if sc(n, 25).value == "Yes" and sc(n, 1).value in gl:
                        gl.remove(sc(n, 1).value)

    if len(gl) > 1:
        for n in range(2, pnum):
            if sc(n, 1).value in gl:
                if sc(n, 4).value == "Yes":
                    dual_type = True
                    answer4 = "yes"
                if sc(n, 4).value == "No":
                    no_dual_type = True
                    answer4 = "no"
        if dual_type:
            if no_dual_type:
                answer4 = input("QUESTION " + str(qcount) + ": Does your Pokemon have a dual typing? ")
                qcount += 1
                if answer4 == "yes":
                    for n in range(2, pnum):
                        if sc(n, 4).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                elif answer4 == "no":
                    for n in range(2, pnum):
                        if sc(n, 4).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def question4b():
        global dual_type_evo
        global no_dual_type_evo
        global qcount
        global true_false4b
        true_false4b = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 26).value == "Yes":
                        dual_type_evo = True
                    if sc(n, 26).value == "No":
                        no_dual_type_evo = True
            if dual_type_evo:
                if no_dual_type_evo:
                    if evolves:
                        answer4b = input("QUESTION " + str(qcount) + ": Does your Pokemon have a dual typing when "
                                                                     "fully evolved? ")
                        qcount += 1
                        if answer4b == "yes":
                            for n in range(2, pnum):
                                if sc(n, 26).value == "No" and sc(n, 1).value in gl:
                                    gl.remove(sc(n, 1).value)
                        elif answer4b == "no":
                            for n in range(2, pnum):
                                if sc(n, 26).value == "Yes" and sc(n, 1).value in gl:
                                    gl.remove(sc(n, 1).value)


    def question5():
        global starter
        global qcount
        global true_false5
        true_false5 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 8).value == "Yes":
                        starter = True
            if starter:
                if evolves or evolved:
                    answer5 = input("QUESTION " + str(qcount) + ": Is your Pokemon part of a starter evolution line? ")
                    qcount += 1
                    if answer5 == "yes":
                        for n in range(2, pnum):
                            if sc(n, 8).value =="No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                    elif answer5 == "no":
                        for n in range(2, pnum):
                            if sc(n, 8).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    def question6():
        global breed
        global non_breed
        global qcount
        global true_false6
        true_false6 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 10).value == "No":
                        non_breed = True
                    if sc(n, 10).value == "Yes":
                        breed = True
            if non_breed:
                if breed:
                    answer6 = input("QUESTION " + str(qcount) + ": Can your Pokemon breed with a Ditto? ")
                    qcount += 1
                    if answer6 == "yes":
                        for n in range(2, pnum):
                            if sc(n, 10).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                    elif answer6 == "no":
                        for n in range(2, pnum):
                            if sc(n, 10).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    def question7():
        global legend
        global non_legend
        global qcount
        global true_false7
        true_false7 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 9).value == "Yes":
                        legend = True
                    if sc(n, 9).value == "No":
                        non_legend = True
            if legend:
                if non_legend:
                    answer7 = input("QUESTION " + str(qcount) + ": Is your Pokemon a legendary? ")
                    qcount += 1
                    if answer7 == "yes":
                        for n in range(2, pnum):
                            if sc(n, 9).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                    elif answer7 == "no":
                        for n in range(2, pnum):
                            if sc(n, 9).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    def question8():
        global mega
        global non_mega
        global qcount
        global true_false8
        true_false8 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 11).value == "Yes":
                        mega = True
                    if sc(n, 11).value == "No":
                        non_mega = True
            if mega:
                if non_mega:
                    if answer2 == "no":
                        answer8 = input("QUESTION " + str(qcount) + ": Can your Pokemon Mega evolve? ")
                        qcount += 1
                        if answer8 == "yes":
                            for n in range(2, pnum):
                                if sc(n, 11).value == "No" and sc(n, 1).value in gl:
                                    gl.remove(sc(n, 1).value)
                        elif answer8 == "no":
                            for n in range(2, pnum):
                                if sc(n, 11).value == "Yes" and sc(n, 1).value in gl:
                                    gl.remove(sc(n, 1).value)


    def question8b():
        global qcount
        global true_false8b
        true_false8b = False
        if len(gl) > 1:
            if answer2 == "yes":
                answer8b = input("QUESTION " + str(qcount) + ": When fully evolved, can your Pokemon Mega evolve? ")
                qcount += 1
                if answer8b == "yes":
                    for n in range(2, pnum):
                        if sc(n, 24).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                elif answer8b == "no":
                    for n in range(2, pnum):
                        if sc(n, 24).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def question9():
        global gmax_evo
        global qcount
        global true_false9
        true_false9 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 27).value == "Yes":
                        gmax_evo = True
            if gmax_evo:
                answer9 = input("QUESTION " + str(qcount) + ": When fully evolved, does your Pokemon's have a "
                                                            "Gigantamax form? ")
                qcount += 1
                if answer9 == "yes":
                    for n in range(2, pnum):
                        if sc(n, 27).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                elif answer9 == "no":
                    for n in range(2, pnum):
                        if sc(n, 27).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def question9b():
        global gmax
        global qcount
        global true_false9b
        true_false9b = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 12).value == "Yes":
                        gmax = True
            if gmax:
                answer9b = input("QUESTION " + str(qcount) + ": Does your Pokemon have a Gigantamax form? ")
                qcount += 1
                if answer9b == "yes":
                    for n in range(2, pnum):
                        if sc(n, 12).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                elif answer9b == "no":
                    for n in range(2, pnum):
                        if sc(n, 12).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def question10():
        global branched
        global qcount
        global true_false10
        true_false10 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 14).value == "Yes":
                        branched = True
            if branched:
                if answer2 or answer3 != "no":
                    answer10 = input("QUESTION " + str(qcount) + ": Does your Pokemon's evolution line contain any "
                                                                 "branched evolutions? ")
                    qcount += 1
                    if answer10 == "yes":
                        for n in range(2, pnum):
                            if sc(n, 14).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                    elif answer10 == "no":
                        for n in range(2, pnum):
                            if sc(n, 14).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    def question11():
        global cross_g
        global n
        global qcount
        global true_false11
        true_false11 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 15).value == "Yes":
                        cross_g = True
            if cross_g:
                if answer2 or answer3 != "no":
                    answer11 = input("QUESTION " + str(qcount) + ": Does your Pokemon's evolution line have any "
                                                                 "cross-generational evolutions? ")
                    qcount += 1
                    if answer11 == "yes":
                        for n in range(2, pnum):
                            if sc(n, 15).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                    elif answer11 == "no":
                        for n in range(2, pnum):
                            if sc(n, 15).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    def question12():
        global regional
        global qcount
        global true_false12
        true_false12 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 13).value == "Yes":
                        regional = True
            if regional:
                answer12 = input("QUESTION " + str(qcount) + ": Does your Pokemon have a regional variant? ")
                qcount += 1
                for n in range(2, pnum):
                    if answer12 == "yes":
                        if sc(n, 13).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                    elif answer12 == "no":
                        if sc(n, 13).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                            regional = False


    def question12b():
        global evo_regional
        global qcount
        global true_false12b
        true_false12b = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 22).value == "Yes":
                        evo_regional = True
            if evo_regional:
                if not regional:
                    answer12b = input("QUESTION " + str(qcount) + ": Does any of your Pokemon's evolution line have "
                                                                  "regional variants? ")
                    qcount += 1
                    for n in range(2, pnum):
                        if answer12b == "yes":
                            if sc(n, 22).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                        elif answer12b == "no":
                            if sc(n, 22).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    def question13():
        global multi_head
        global qcount
        global true_false13
        true_false13 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 16).value == "Yes":
                        multi_head = True
            if multi_head:
                answer13 = input("QUESTION " + str(qcount) + ": Does your Pokemon have multiple heads or faces? ")
                qcount += 1
                if answer13 == "yes":
                    for n in range(2, pnum):
                        if sc(n, 16).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                elif answer13 == "no":
                    for n in range(2, pnum):
                        if sc(n, 16).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def question14():
        global levelup
        global no_levelup
        global qcount
        global true_false14
        true_false14 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 17).value == "Yes":
                        levelup = True
                    if sc(n, 17).value == "No":
                        no_levelup = True
            if evolves:
                if levelup:
                    if no_levelup:
                        answer14 = input("QUESTION " + str(qcount) + ": Does your Pokemon evolve purely by levelling "
                                                                     "up? ")
                        qcount += 1
                        if answer14 == "yes":
                            for n in range(2, pnum):
                                if sc(n, 17).value == "No" and sc(n, 1).value in gl:  # has to be == "No" as
                                    gl.remove(sc(n, 1).value)  # there are other options
                        elif answer14 == "no":
                            for n in range(2, pnum):
                                if sc(n, 17).value == "Yes" and sc(n, 1).value in gl:  # has to be == "Yes" as
                                    gl.remove(sc(n, 1).value)  # there are other options


    def question15():
        global wings
        global no_wings
        global qcount
        global true_false15
        true_false15 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 18).value == "Yes":
                        wings = True
                    if sc(n, 18).value == "No":
                        no_wings = True
            if wings:
                if no_wings:
                    answer15 = input("QUESTION " + str(qcount) + ": Does your Pokemon have wings? ")
                    qcount += 1
                    if answer15 == "yes":
                        for n in range(2, pnum):
                            if sc(n, 18).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                    elif answer15 == "no":
                        for n in range(2, pnum):
                            if sc(n, 18).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    def question16():
        global floating
        global no_floating
        global qcount
        global true_false16
        true_false16 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 19).value == "Yes":
                        floating = True
                    if sc(n, 19).value == "No":
                        no_floating = True
            if floating:
                if no_floating:
                    answer16 = input("QUESTION " + str(qcount) + ": Does your Pokemon float above the ground/water? ")
                    qcount += 1
                    if answer16 == "yes":
                        for n in range(2, pnum):
                            if sc(n, 19).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                    elif answer16 == "no":
                        for n in range(2, pnum):
                            if sc(n, 19).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    def question17():
        global legs
        global no_legs
        global qcount
        global true_false17
        true_false17 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 20).value == "Yes":
                        legs = True
                    if sc(n, 20).value == "No":
                        no_legs = True
            if legs:
                if no_legs:
                    answer17 = input("QUESTION " + str(qcount) + ": Does your Pokemon have legs? ")
                    qcount += 1
                    if answer17 == "yes":
                        for n in range(2, pnum):
                            if sc(n, 20).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                    elif answer17 == "no":
                        for n in range(2, pnum):
                            if sc(n, 20).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    def question18():
        global baby
        global qcount
        global true_false18
        true_false18 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 23).value == "Yes":
                        baby = True
            if baby:
                answer18 = input("QUESTION " + str(qcount) + ": Does your Pokemon have a baby evolution? ")
                qcount += 1
                if answer18 == "yes":
                    for n in range(2, pnum):
                        if sc(n, 23).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                elif answer18 == "no":
                    for n in range(2, pnum):
                        if sc(n, 23).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def question19():
        global foss
        global qcount
        global true_false19
        true_false19 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 28).value == "Yes":
                        foss = True
            if foss:
                answer19 = input("QUESTION " + str(qcount) + ": Does your Pokemon originate from a fossil? ")
                qcount += 1
                for n in range(2, pnum):
                    if answer19 == "yes":
                        if sc(n, 28).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                    elif answer19 == "no":
                        if sc(n, 28).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def question20():
        global type_guess1
        global skip
        global same_type1
        global same_type2
        global next_type
        global qcount
        if len(typ) == 2 * (typ.count(type_guess1)):
            if answer4 == "yes":
                next_type = 2
        typ.clear()
        for n in range(2, pnum):
            if sc(n, 1).value in gl:
                if answer4 == "no":
                    typ.append(sc(n, 2).value)
                if answer4 == "yes":
                    typ.append(sc(n, 2).value)
                    typ.append(sc(n, 3).value)
        type_guess1 = (statistics.mode(typ))
        if answer4 == "yes":
            if len(typ) == 2 * (typ.count(type_guess1)):
                same_type1 = True
        if answer4 == "no":
            if len(typ) != (typ.count(type_guess1)):
                answer20 = input("QUESTION " + str(qcount) + ": Is your Pokemon a " + type_guess1 + " type? ")
                qcount += 1
                if answer20 == "yes":
                    for n in range(2, pnum):
                        if sc(n, 2).value != type_guess1 and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                elif answer20 == "no":
                    for n in range(2, pnum):
                        if sc(n, 2).value == type_guess1 and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)

        if answer4 == "yes":
            if next_type == 1:
                if not same_type1:
                    answer20b = input("QUESTION " + str(qcount) + ": Is your Pokemon part " + type_guess1 + " type? ")
                    qcount += 1
                    if answer20b == "yes":
                        for n in range(2, pnum):
                            if (sc(n, 2).value != type_guess1) and (sc(n, 3).value != type_guess1):
                                if sc(n, 1).value in gl:
                                    gl.remove(sc(n, 1).value)
                                    next_type = 2
                    elif answer20b == "no":
                        for n in range(2, pnum):
                            if sc(n, 1).value in gl:
                                if (sc(n, 2).value == type_guess1) or (sc(n, 3).value == type_guess1):
                                    gl.remove(sc(n, 1).value)


    def question22():
        global typ2
        global type_guess1
        global type_guess2
        global qcount
        if next_type == 2:
            global same_type2
            typ.clear()
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    typ.append(sc(n, 2).value)
                    typ.append(sc(n, 3).value)
            type_guess1 = (statistics.mode(typ))
            typ2 = []
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 2).value == type_guess1:
                        typ2.append(sc(n, 3).value)
                    elif sc(n, 3).value == type_guess1:
                        typ2.append(sc(n, 2).value)
            type_guess2 = (statistics.mode(typ2))
            if len(typ2) == (typ2.count(type_guess2)):
                same_type2 = True

            if not same_type2:
                answer22 = input("QUESTION " + str(qcount) + ": Is your Pokemon part " + type_guess2 + " type? ")
                qcount += 1
                if answer22 == "yes":
                    for n in range(2, pnum):
                        if (sc(n, 2).value != type_guess2) and (sc(n, 3).value != type_guess2):
                            if sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                elif answer22 == "no":
                    for n in range(2, pnum):
                        if sc(n, 1).value in gl:
                            if (sc(n, 2).value == type_guess2) or (sc(n, 3).value == type_guess2):
                                gl.remove(sc(n, 1).value)


    def question21():
        global tail
        global no_tail
        global evo_tail
        global no_evo_tail
        global qcount
        global true_false21
        true_false21 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 29).value == "Yes":
                        tail = True
                    if sc(n, 29).value == "No":
                        no_tail = True
            if tail:
                if no_tail:
                    answer21 = input("QUESTION " + str(qcount) + ": Does your Pokemon have a tail? ")
                    qcount += 1
                    for n in range(2, pnum):
                        if answer21 == "yes":
                            if sc(n, 29).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                        elif answer21 == "no":
                            if sc(n, 29).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                                tail = False


    def question21b():
        global tail
        global no_tail
        global evo_tail
        global no_evo_tail
        global qcount
        global true_false21b
        true_false21b = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 30).value == "Yes":
                        evo_tail = True
                    if sc(n, 30).value == "No":
                        no_evo_tail = True
            if evo_tail:
                if no_evo_tail:
                    if not tail:
                        answer21b = input("QUESTION " + str(qcount) + ": Does any of your Pokemon's evolution line "
                                                                      "have a tail? ")
                        qcount += 1
                        for n in range(2, pnum):
                            if answer21b == "yes":
                                if sc(n, 30).value == "No" and sc(n, 1).value in gl:
                                    gl.remove(sc(n, 1).value)
                            elif answer21b == "no":
                                if sc(n, 30).value == "Yes" and sc(n, 1).value in gl:
                                    gl.remove(sc(n, 1).value)


    def question23():
        global male_only
        global female_only
        global mixed_gender
        global genderless
        global skip
        global qcount
        global true_false23
        true_false23 = False
        gender()
        if len(gl) > 1:
            if ask_male:
                answer23 = input("QUESTION " + str(qcount) + ": Can your Pokemon be male? ")
                qcount += 1
                for n in range(2, pnum):
                    if answer23 == "yes":
                        if sc(n, 31).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                    elif answer23 == "no":
                        if sc(n, 31).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)

        male_only = False
        female_only = False
        mixed_gender = False
        genderless = False


    def question24():
        global male_only
        global female_only
        global mixed_gender
        global genderless
        global skip
        global qcount
        global true_false24
        true_false24 = False
        gender()
        if len(gl) > 1:
            if ask_female:
                answer24 = input("QUESTION " + str(qcount) + ": Can your Pokemon be female? ")
                qcount += 1
                for n in range(2, pnum):
                    if answer24 == "yes":
                        if sc(n, 32).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                    elif answer24 == "no":
                        if sc(n, 32).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)

        male_only = False
        female_only = False
        mixed_gender = False
        genderless = False


    def question24b():
        global male_only
        global female_only
        global mixed_gender
        global genderless
        global skip
        global qcount
        global true_false24b
        true_false24b = False
        gender()
        if len(gl) > 1:
            if ask_genderless:
                answer24b = input("QUESTION " + str(qcount) + ": Is your Pokemon genderless? ")
                qcount += 1
                for n in range(2, pnum):
                    if answer24b == "yes":
                        if sc(n, 33).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                    elif answer24b == "no":
                        if sc(n, 33).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def question25():
        global horn
        global no_horn
        global qcount
        global true_false25
        true_false25 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 36).value == "Yes":
                        horn = True
                    if sc(n, 36).value == "No":
                        no_horn = True
            if horn:
                if no_horn:
                    answer25 = input("QUESTION " + str(qcount) + ": Does your Pokemon have a horn? ")
                    qcount += 1
                    for n in range(2, pnum):
                        if answer25 == "yes":
                            if sc(n, 36).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                        elif answer25 == "no":
                            if sc(n, 36).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    def question26():
        global same_color1
        global skip
        global n
        global qcount
        dex_color.clear()
        for n in range(2, pnum):
            if sc(n, 1).value in gl:
                dex_color.append(sc(n, 41).value)
        color_guess1 = (statistics.mode(dex_color))
        if len(dex_color) == (dex_color.count(color_guess1)):
            same_color1 = True

        if len(dex_color) != (dex_color.count(color_guess1)):
            if not same_color1:
                answer26 = input("QUESTION " + str(qcount) + ": Is your Pokemon's Pokedex color " + color_guess1 + "? ")
                qcount += 1
                if answer26 == "yes":
                    for n in range(2, pnum):
                        if sc(n, 41).value != color_guess1 and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)

                elif answer26 == "no":
                    for n in range(2, pnum):
                        if sc(n, 41).value == color_guess1 and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def questionx1():
        global pre_gmax
        global qcount
        global true_false27
        true_false27 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 34).value == "Yes":
                        pre_gmax = True
            if pre_gmax:
                answer_extra1 = input("QUESTION " + str(qcount) + ": Can your Pokemon's pre-evolution Gigantamax? ")
                qcount += 1
                for n in range(2, pnum):
                    if answer_extra1 == "yes":
                        if sc(n, 34).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                    elif answer_extra1 == "no":
                        if sc(n, 34).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def questionx2():
        global gloves
        global qcount
        global true_false28
        true_false28 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 35).value == "Yes":
                        gloves = True
            if gloves:
                answer_extra2 = input("QUESTION " + str(qcount) + ": Does your Pokemon appear to be wearing gloves? ")
                qcount += 1
                for n in range(2, pnum):
                    if answer_extra2 == "yes":
                        if sc(n, 35).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                    elif answer_extra2 == "no":
                        if sc(n, 35).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def questionx3():
        global any_move
        global qcount
        global true_false29
        true_false29 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 37).value == "Yes":
                        any_move = True
            if any_move:
                answer_extra3 = input("QUESTION " + str(qcount) + ": Can your Pokemon learn almost any move with "
                                                                  "Sketch? ")
                qcount += 1
                for n in range(2, pnum):
                    if answer_extra3 == "yes":
                        if sc(n, 37).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                    elif answer_extra3 == "no":
                        if sc(n, 37).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def questionx4():
        global bear
        global qcount
        global true_false30
        true_false30 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 38).value == "Yes":
                        bear = True
            if bear:
                answer_extra4 = input("QUESTION " + str(qcount) + ": Is your Pokemon similar to a bear? ")
                qcount += 1
                for n in range(2, pnum):
                    if answer_extra4 == "yes":
                        if sc(n, 38).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                    elif answer_extra4 == "no":
                        if sc(n, 38).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def questionx5():
        global color_change
        global qcount
        global true_false31
        true_false31 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 39).value == "Yes":
                        if sc(n, 1).value == "Kecleon":
                            color_change = True
            if color_change:
                answer_extra5 = input("QUESTION " + str(qcount) + ": Can your Pokemon change color? ")
                qcount += 1
                for n in range(2, pnum):
                    if answer_extra5 == "yes":
                        if sc(n, 39).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                    elif answer_extra5 == "no":
                        if sc(n, 39).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def questionx6():
        global third_evo
        global not_third_evo
        global qcount
        global true_false32
        true_false32 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 40).value == "Yes":
                        third_evo = True
                    if sc(n, 40).value == "No":
                        not_third_evo = True
            if third_evo:
                if not_third_evo:
                    answer_extra6 = input("QUESTION " + str(qcount) + ": Is your Pokemon the third in its evolution "
                                                                      "line? ")
                    qcount += 1
                    for n in range(2, pnum):
                        if answer_extra6 == "yes":
                            if sc(n, 40).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                        elif answer_extra6 == "no":
                            if sc(n, 40).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    def questionx7():
        global minus_cheeks
        global qcount
        global true_false33
        true_false33 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 42).value == "Yes":
                        minus_cheeks = True
            if minus_cheeks:
                answer_extra7 = input("QUESTION " + str(qcount) + ": Does your Pokemon have minus signs on its cheeks? ")
                qcount += 1
                for n in range(2, pnum):
                    if answer_extra7 == "yes":
                        if sc(n, 42).value == "No" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)
                    elif answer_extra7 == "no":
                        if sc(n, 42).value == "Yes" and sc(n, 1).value in gl:
                            gl.remove(sc(n, 1).value)


    def questionx8():
        global pre_evo_type
        global no_pre_evo_type
        global qcount
        global true_false34
        true_false34 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 43).value == "Yes":
                        pre_evo_type = True
                    if sc(n, 43).value == "No":
                        no_pre_evo_type = True
            if pre_evo_type:
                if no_pre_evo_type:
                    answer_extra8 = input("QUESTION " + str(qcount) + ": Does your Pokemon's pre-evolution have a "
                                                                      "different typing? ")
                    qcount += 1
                    for n in range(2, pnum):
                        if answer_extra8 == "yes":
                            if sc(n, 43).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                        elif answer_extra8 == "no":
                            if sc(n, 43).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    def questionx9():
        global evo_type_change
        global no_evo_type_change
        global qcount
        global true_false35
        true_false35 = False
        if len(gl) > 1:
            for n in range(2, pnum):
                if sc(n, 1).value in gl:
                    if sc(n, 44).value == "Yes":
                        evo_type_change = True
                    if sc(n, 44).value == "No":
                        no_evo_type_change = True
            if evo_type_change:
                if no_evo_type_change:
                    answer_extra9 = input("QUESTION " + str(qcount) + ": Does your Pokemon change typing when it "
                                                                      "evolves? ")
                    qcount += 1
                    for n in range(2, pnum):
                        if answer_extra9 == "yes":
                            if sc(n, 44).value == "No" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)
                        elif answer_extra9 == "no":
                            if sc(n, 44).value == "Yes" and sc(n, 1).value in gl:
                                gl.remove(sc(n, 1).value)


    breakout = 0
    while len(gl) > 1 and breakout == 0:
        while len(gl) > 1 and enter_question_decider:
            print("Remaining Pokemon = " + str(len(gl)))
            # QUESTION 4b - Dual_type_evo
            if true_false4b:                                       ######### Not sure if question works, may need moving
                yes_no.clear()                                     ######### back to a mandatory question
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 26).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating4b = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating4b = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating4b = len(gl) + 1 - either_count
                if importance_rating4b > importance_ratingx:
                    next_question = 4.5
                    importance_ratingx = importance_rating4b

            # QUESTION 5 - Starter
            importance_ratingx = 0
            if true_false5:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 8).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating5 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating5 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating5 = len(gl) + 1 - either_count
                if importance_rating5 > importance_ratingx:
                    next_question = 5
                    importance_ratingx = importance_rating5

            # QUESTION 6 - Breed
            if true_false6:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 10).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating6 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating6 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating6 = len(gl) + 1 - either_count
                if importance_rating6 > importance_ratingx:
                    next_question = 6
                    importance_ratingx = importance_rating6

            # QUESTION 7 - Legend
            if true_false7:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 9).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating7 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating7 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating7 = len(gl) + 1 - either_count
                if importance_rating7 > importance_ratingx:
                    next_question = 7
                    importance_ratingx = importance_rating7

            # QUESTION 8 - Mega
            if true_false8:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 11).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating8 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating8 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating8 = len(gl) + 1 - either_count
                if importance_rating8 > importance_ratingx:
                    next_question = 8
                    importance_ratingx = importance_rating8

            # QUESTION 8b - evo_mega
            if true_false8b:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 24).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating8b = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating8b = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating8b = len(gl) + 1 - either_count
                if importance_rating8b > importance_ratingx:
                    next_question = 8.5
                    importance_ratingx = importance_rating8b

            # QUESTION 9 - Gmax_evo
            if true_false9:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 27).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating9 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating9 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating9 = len(gl) + 1 - either_count
                if importance_rating9 > importance_ratingx:
                    next_question = 9
                    importance_ratingx = importance_rating9

            # QUESTION 9b - Gmax
            if true_false9b:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 12).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating9b = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating9b = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating9b = len(gl) + 1 - either_count
                if importance_rating9b > importance_ratingx:
                    next_question = 9.5
                    importance_ratingx = importance_rating9b

            # QUESTION 10 - Branched
            if true_false10:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 14).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating10 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating10 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating10 = len(gl) + 1 - either_count
                if importance_rating10 > importance_ratingx:
                    next_question = 10
                    importance_ratingx = importance_rating10

            # QUESTION 11 - Cross_g
            if true_false11:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 15).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating11 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating11 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating11 = len(gl) + 1 - either_count
                if importance_rating11 > importance_ratingx:
                    next_question = 11
                    importance_ratingx = importance_rating11

            # QUESTION 12 - Regional
            if true_false12:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 13).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating12 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating12 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating12 = len(gl) + 1 - either_count
                if importance_rating12 > importance_ratingx:
                    next_question = 12
                    importance_ratingx = importance_rating12

            # QUESTION 12b - Evo_regional
            if true_false12b:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 22).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating12b = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating12b = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating12b = len(gl) + 1 - either_count
                if importance_rating12b > importance_ratingx:
                    next_question = 12.5
                    importance_ratingx = importance_rating12b

            # QUESTION 13 - Multi_head
            if true_false13:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 16).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating13 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating13 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating13 = len(gl) + 1 - either_count
                if importance_rating13 > importance_ratingx:
                    next_question = 13
                    importance_ratingx = importance_rating13

            # QUESTION 14 - Levelup
            if true_false14:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 17).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating14 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating14 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating14 = len(gl) + 1 - either_count
                if importance_rating14 > importance_ratingx:
                    next_question = 14
                    importance_ratingx = importance_rating14

            # QUESTION 15 - Wings
            if true_false15:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 18).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating15 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating15 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating15 = len(gl) + 1 - either_count
                if importance_rating15 > importance_ratingx:
                    next_question = 15
                    importance_ratingx = importance_rating15

            # QUESTION 16 - Floating
            if true_false16:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 19).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating16 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating16 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating16 = len(gl) + 1 - either_count
                if importance_rating16 > importance_ratingx:
                    next_question = 16
                    importance_ratingx = importance_rating16

            # QUESTION 17 - Legs
            if true_false17:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 20).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating17 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating17 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating17 = len(gl) + 1 - either_count
                if importance_rating17 > importance_ratingx:
                    next_question = 17
                    importance_ratingx = importance_rating17

            # QUESTION 18 - Baby
            if true_false18:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 23).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating18 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating18 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating18 = len(gl) + 1 - either_count
                if importance_rating18 > importance_ratingx:
                    next_question = 18
                    importance_ratingx = importance_rating18

            # QUESTION 19 - Foss
            if true_false19:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 28).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating19 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating19 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating19 = len(gl) + 1 - either_count
                if importance_rating19 > importance_ratingx:
                    next_question = 19
                    importance_ratingx = importance_rating19

            # QUESTION 20 & 22 - Type
            if true_false20:  # Might be able to delete TF20
                typ.clear()
                typ = []
                if next_type == 1:
                    for x in range(2, pnum):
                        if sc(x, 1).value in gl:
                            if answer4 == "no":
                                typ.append(sc(x, 2).value)
                            if answer4 == "yes":
                                typ.append(sc(x, 2).value)
                                typ.append(sc(x, 3).value)
                    type_guess1 = (statistics.mode(typ))
                    if answer4 == "no":
                        yes_count = typ.count(type_guess1)
                        no_count = len(typ) - yes_count
                    if answer4 == "yes":
                        yes_count = 2 * (typ.count(type_guess1))
                        no_count = int(len(typ) / 2)

                    if yes_count >= no_count:
                        importance_rating20 = len(gl) + 0 - int(yes_count - no_count)
                    elif no_count >= yes_count:
                        importance_rating20 = len(gl) + 0 - int(no_count - yes_count)
                    else:
                        importance_rating20 = len(gl) + 0
                    if importance_rating20 > importance_ratingx:
                        next_question = 20
                        importance_ratingx = importance_rating20

                elif next_type == 2:
                    for n in range(2, pnum):
                        if sc(n, 1).value in gl:
                            if answer4 == "no":
                                typ.append(sc(n, 2).value)
                            if answer4 == "yes":
                                typ.append(sc(n, 2).value)
                                typ.append(sc(n, 3).value)
                    type_guess1 = (statistics.mode(typ))

                    if answer4 == "yes":
                        typ2 = []
                        for n in range(2, pnum):
                            if sc(n, 1).value in gl:
                                if sc(n, 2).value == type_guess1:
                                    typ2.append(sc(n, 3).value)
                                elif sc(n, 3).value == type_guess1:
                                    typ2.append(sc(n, 2).value)
                        type_guess2 = (statistics.mode(typ2))
                        if len(typ2) == (typ2.count(type_guess2)):
                            same_type2 = True

                        if not same_type2:
                            yes_count = typ2.count(type_guess2)
                            no_count = len(typ2) - yes_count
                            if yes_count >= no_count:
                                importance_rating22 = len(gl) + 0 - int(yes_count - no_count)
                            elif no_count >= yes_count:
                                importance_rating22 = len(gl) + 0 - int(no_count - yes_count)
                            else:
                                importance_rating22 = len(gl) + 0
                            if importance_rating22 > importance_ratingx:
                                next_question = 22
                                importance_ratingx = importance_rating22

            # QUESTION 21 - Tail
            if true_false21:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 29).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating21 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating21 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating21 = len(gl) + 1 - either_count
                if importance_rating21 > importance_ratingx:
                    next_question = 21
                    importance_ratingx = importance_rating21

            # QUESTION 21b - Evo_tail
            if true_false21b:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 30).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating21b = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating21b = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating21b = len(gl) + 1 - either_count
                if importance_rating21b > importance_ratingx:
                    next_question = 21.5
                    importance_ratingx = importance_rating21b

            # QUESTION 23 - Male
            if true_false23:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 31).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating23 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating23 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating23 = len(gl) + 1 - either_count
                if importance_rating23 > importance_ratingx:
                    next_question = 23
                    importance_ratingx = importance_rating23

            # QUESTION 24 - Female
            if true_false24:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 32).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating24 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating24 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating24 = len(gl) + 1 - either_count
                if importance_rating24 > importance_ratingx:
                    next_question = 24
                    importance_ratingx = importance_rating24

            # QUESTION 24b - Genderless
            if true_false24b:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 33).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating24b = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating24b = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_rating24b = len(gl) + 1 - either_count
                if importance_rating24b > importance_ratingx:
                    next_question = 24.5
                    importance_ratingx = importance_rating24b

            # QUESTION 25 - Horn
            if true_false25:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 36).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_rating25 = len(gl) + 0 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_rating25 = len(gl) + 0 - int(no_count - yes_count - either_count)
                else:
                    importance_rating25 = len(gl) + 0 - either_count
                if importance_rating25 > importance_ratingx:
                    next_question = 25
                    importance_ratingx = importance_rating25

            # QUESTION26 - Color
            if true_false26:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 41).value)
                color_guess = (statistics.mode(yes_no))
                yes_count = yes_no.count(color_guess)
                no_count = len(yes_no) - yes_count
                if yes_count >= no_count:
                    importance_rating26 = len(gl) + 0 - int(yes_count - no_count)
                elif no_count >= yes_count:
                    importance_rating26 = len(gl) + 0 - int(no_count - yes_count)
                else:
                    importance_rating26 = len(gl) + 0
                if importance_rating26 > importance_ratingx:
                    next_question = 26
                    importance_ratingx = importance_rating26

            # QUESTIONX1 - Pre_gmax
            if true_false27:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 34).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_ratingx1 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_ratingx1 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_ratingx1 = len(gl) + 1 - either_count
                if importance_ratingx1 > importance_ratingx:
                    next_question = 27
                    importance_ratingx = importance_ratingx1

            # QUESTIONX2 - Gloves
            if true_false28:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 35).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_ratingx2 = len(gl) + 0 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_ratingx2 = len(gl) + 0 - int(no_count - yes_count - either_count)
                else:
                    importance_ratingx2 = len(gl) + 0 - either_count
                if importance_ratingx2 > importance_ratingx:
                    next_question = 28
                    importance_ratingx = importance_ratingx2

            # QUESTIONX3 - Any_move
            if true_false29:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 37).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_ratingx3 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_ratingx3 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_ratingx3 = len(gl) + 1 - either_count
                if importance_ratingx3 > importance_ratingx:
                    next_question = 29
                    importance_ratingx = importance_ratingx3

            # QUESTIONX4 - Bear
            if true_false30:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 38).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_ratingx4 = len(gl) + 0 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_ratingx4 = len(gl) + 0 - int(no_count - yes_count - either_count)
                else:
                    importance_ratingx4 = len(gl) + 0 - either_count
                if importance_ratingx4 > importance_ratingx:
                    next_question = 30
                    importance_ratingx = importance_ratingx4

            # QUESTIONX5 - Color_change
            if true_false31:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 39).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_ratingx5 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_ratingx5 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_ratingx5 = len(gl) + 1 - either_count
                if importance_ratingx5 > importance_ratingx:
                    next_question = 31
                    importance_ratingx = importance_ratingx5

            # QUESTIONX6 - Third_evo
            if true_false32:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 40).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_ratingx6 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_ratingx6 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_ratingx6 = len(gl) + 1 - either_count
                if importance_ratingx6 > importance_ratingx:
                    next_question = 32
                    importance_ratingx = importance_ratingx6

            # QUESTIONX7 - Minus_cheeks
            if true_false33:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 42).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_ratingx7 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_ratingx7 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_ratingx7 = len(gl) + 1 - either_count
                if importance_ratingx7 > importance_ratingx:
                    next_question = 33
                    importance_ratingx = importance_ratingx7

            # QUESTIONX8 - Pre_evo_type
            if true_false34:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 43).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_ratingx8 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_ratingx8 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_ratingx8 = len(gl) + 1 - either_count
                if importance_ratingx8 > importance_ratingx:
                    next_question = 34
                    importance_ratingx = importance_ratingx8

            # QUESTIONX9 - Evo_type_change
            if true_false35:
                yes_no.clear()
                yes_no = []
                for x in range(2, pnum):
                    if sc(x, 1).value in gl:
                        yes_no.append(sc(x, 44).value)
                yes_count = yes_no.count("Yes")
                no_count = yes_no.count("No")
                either_count = yes_no.count("Yes/No")
                if yes_count >= no_count:
                    importance_ratingx9 = len(gl) + 1 - int(yes_count - no_count - either_count)
                elif no_count >= yes_count:
                    importance_ratingx9 = len(gl) + 1 - int(no_count - yes_count - either_count)
                else:
                    importance_ratingx9 = len(gl) + 1 - either_count
                if importance_ratingx9 > importance_ratingx:
                    next_question = 35
                    importance_ratingx = importance_ratingx9

            enter_question_decider = False

        breakout = 1

        if next_question == 4.5:
            breakout = 0
            question4b()
        if next_question == 5:
            breakout = 0
            question5()
        if next_question == 6:
            breakout = 0
            question6()
        if next_question == 7:
            breakout = 0
            question7()
        if next_question == 8:
            breakout = 0
            question8()
        if next_question == 8.5:
            breakout = 0
            question8b()
        if next_question == 9:
            breakout = 0
            question9()
        if next_question == 9.5:
            breakout = 0
            question9b()
        if next_question == 10:
            breakout = 0
            question10()
        if next_question == 11:
            breakout = 0
            question11()
        if next_question == 12:
            breakout = 0
            question12()
        if next_question == 12.5:
            breakout = 0
            question12b()
        if next_question == 13:
            breakout = 0
            question13()
        if next_question == 14:
            breakout = 0
            question14()
        if next_question == 15:
            breakout = 0
            question15()
        if next_question == 16:
            breakout = 0
            question16()
        if next_question == 17:
            breakout = 0
            question17()
        if next_question == 18:
            breakout = 0
            question18()
        if next_question == 19:
            breakout = 0
            question19()
        if next_question == 20:
            breakout = 0
            question20()
        if next_question == 21:
            breakout = 0
            question21()
        if next_question == 21.5:
            breakout = 0
            question21b()
        if next_question == 22:
            breakout = 0
            question22()
        if next_question == 23:
            breakout = 0
            question23()
        if next_question == 24:
            breakout = 0
            question24()
        if next_question == 24.5:
            breakout = 0
            question24b()
        if next_question == 25:
            breakout = 0
            question25()
        if next_question == 26:
            breakout = 0
            question26()
        if next_question == 27:
            breakout = 0
            questionx1()
        if next_question == 28:
            breakout = 0
            questionx2()
        if next_question == 29:
            breakout = 0
            questionx3()
        if next_question == 30:
            breakout = 0
            questionx4()
        if next_question == 31:
            breakout = 0
            questionx5()
        if next_question == 32:
            breakout = 0
            questionx6()
        if next_question == 33:
            breakout = 0
            questionx7()
        if next_question == 34:
            breakout = 0
            questionx8()
        if next_question == 35:
            breakout = 0
            questionx9()

        next_question = None
        if breakout == 0:
            enter_question_decider = True

    # QUESTIONX10 - Region
    if len(gl) > 1:
        yes_no.clear()
        yes_no = []
        for x in range(2, pnum):
            if sc(x, 1).value in gl:
                yes_no.append(sc(x, 7).value)
        region_guess = (statistics.mode(yes_no))
        answer_extra10 = input("QUESTION " + str(qcount) + ": Is your Pokemon from the " + region_guess + " region? ")
        qcount += 1
        if answer_extra10 == "yes":
            for n in range(2, pnum):
                if sc(n, 7).value != region_guess and sc(n, 1).value in gl:
                    gl.remove(sc(n, 1).value)
        elif answer_extra10 == "no":
            for n in range(2, pnum):
                if sc(n, 7).value == region_guess and sc(n, 1).value in gl:
                    gl.remove(sc(n, 1).value)

    if len(gl) == 1:
        final_guess = input("FINAL QUESTION: Is your Pokemon " + str(*gl) + "? ")

        if final_guess == "yes":
            play_again = input("Excellent! I guessed your Pokemon in " + str(qcount) + " guesses! I hope you enjoyed "
                                                                                       "playing, "
                                                                                       "would you like to play again? ")
            if play_again == "yes":
                print("""
                
                
                """)
            if play_again == "no":
                print("Okay, thanks for playing! ")
                play = False

        elif final_guess == "no":
            try_again = input("Hmmm, please consult the chart and lets try again, okay? ")
            if try_again == "yes":
                print("""


                                """)
            if try_again == "no":
                print("Okay, thanks for playing! ")
                play = False

    elif len(gl) > 1:
        print(gl)  ####### DONT LEAVE THIS IN ########

    else:
        try_again = input("Hmmm, please consult the chart and lets try again, okay? ")
        if try_again == "yes":
            print("""


                            """)
        if try_again == "no":
            print("Okay, thanks for playing! ")
            play = False
