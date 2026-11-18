def run_optical_illusion_quiz():
    print("=" * 65)
    print("QUERY #002: THE OPTICAL ILLUSION OF CONSENSUS")
    print("The Human Variable Lab | Based on Solomon Asch (1951)")
    print("=" * 65)
    print("A 30-second interactive experiment testing modern intuition")
    print("against a classic study on group pressure and conformity.\n")

    # --- QUESTION 1: Baseline Conformity ---
    print("QUESTION 1:")
    print("You clearly see that Line A matches the target line. However,")
    print("everyone else at the table confidently calls out 'Line B' before")
    print("it reaches you. What do you say out loud?")
    print("  1. Say 'Line A' and stand by what my own eyes see.")
    print("  2. Say 'Line B' to avoid awkwardness, even though I know it is wrong.")
    print("  3. Say 'Line B' because I assume the group must see something I missed.")
    q1 = int(input("Enter 1, 2, or 3: "))
    print()

    # --- QUESTION 2: Public Compliance vs. Private Belief ---
    print("QUESTION 2:")
    print("If the researcher allowed you to write your answer down privately")
    print("on paper instead of speaking out loud, how much more likely would")
    print("you be to stick with Line A?")
    print("  Scale: 1 (No difference, I would answer the same) to 5 (Much more likely)")
    q2 = int(input("Enter a number from 1 to 5: "))
    print()

    # --- QUESTION 3: The Single Dissenter Effect ---
    print("QUESTION 3:")
    print("Imagine just ONE other person at the table breaks unanimity and says")
    print("'Line A' before your turn. How does that affect you?")
    print("  1. It makes it dramatically easier for me to speak up and say 'Line A'.")
    print("  2. It has zero impact on me; I decide independently either way.")
    print("  3. I would still feel pressured to agree with the larger majority.")
    q3 = int(input("Enter 1, 2, or 3: "))
    print()

    # --- QUESTION 4: Confidence in Personal Independence ---
    print("QUESTION 4:")
    print("How confident are you that you would NEVER cave to group pressure")
    print("when an objective fact is right in front of your eyes?")
    print("  Scale: 1 (Not confident, group pressure is strong) to 5 (100% immune)")
    q4 = int(input("Enter a number from 1 to 5: "))
    print()

    # --- SCORING LOGIC (Boolean multiplication & basic arithmetic) ---
    # Higher score = higher susceptibility to social consensus pressure (0 to 100)
    q1_points = (q1 == 1) * 0 + (q1 == 2) * 35 + (q1 == 3) * 50
    q2_points = (q2 - 1) * 5
    q3_points = (q3 == 2) * 0 + (q3 == 1) * 10 + (q3 == 3) * 30
    conformity_index = q1_points + q2_points + q3_points

    print("=" * 65)
    print("YOUR RESULTS VS. ASCH'S 1951 LABORATORY DATA")
    print("=" * 65)
    print("Your Social Consensus Susceptibility Score: " + str(conformity_index) + " / 100\n")

    # 1. Baseline comparison
    print("[1] THE RIGGED ROOM:")
    if q1 == 1:
        print("-> You stood firm on Line A. In Solomon Asch's original 1951 trials,")
        print("   only 25% of participants defied the crowd across every single round.")
        print("   A massive 75% conformed and gave the wrong answer at least once.")
    elif q1 == 2:
        print("-> You experienced what Asch called 'Distortion of Action': you knew")
        print("   Line A was right, yet spoke a lie purely to avoid standing out.")
        print("   Across all trials, participants yielded to the majority 36.8% of the time.")
    else:
        print("-> You experienced 'Distortion of Judgment': the unified front made")
        print("   you doubt your own eyes and assume the crowd knew better. In rare")
        print("   cases, participants even altered their actual visual perception.")
    print()

    # 2. Private vs. Public comparison
    print("[2] PRIVATE BELIEF VS. PUBLIC COMPLIANCE:")
    if q2 >= 4:
        print("-> Your intuition matches Asch's findings. When participants were")
        print("   allowed to write answers down privately instead of speaking aloud,")
        print("   conformity plummeted by nearly two-thirds.")
    else:
        print("-> Even if you feel consistent, Asch proved that removing the public")
        print("   spotlight changes everything: writing answers privately cut")
        print("   conformity by nearly two-thirds.")
    print()

    # 3. Single Dissenter comparison
    print("[3] THE POWER OF A SINGLE DISSENTER:")
    if q3 == 1:
        print("-> Spot on. When Asch planted just ONE allied actor to break unanimity,")
        print("   conformity plunged by 80% (dropping from 32% down to just 5%).")
    elif q3 == 2:
        print("-> While you value total independence, Asch showed that having even")
        print("   one single ally breaks the spell of isolation, cutting conformity")
        print("   rates by a massive 80%.")
    else:
        print("-> Surprisingly, unanimity is far more fragile than it looks: even if")
        print("   a single dissenter gave a DIFFERENT wrong answer, conformity still")
        print("   dropped from 32% down to 9%.")
    print()

    # 4. Independence Illusion
    print("[4] THE ILLUSION OF IMMUNITY:")
    if q4 >= 4:
        print("-> Modern culture romanticizes the lone rebel, yet 75% of ordinary")
        print("   participants in Asch's lab yielded at least once when put under")
        print("   live social scrutiny.")
    else:
        print("-> You recognize the quiet gravity of social belonging. As Asch's")
        print("   data shows, it only takes one person speaking up to give everyone")
        print("   else permission to trust their own eyes.")

    print("\nRead the full breakdown at: https://thehumanvariablelab.substack.com/")

# Run the quiz
run_optical_illusion_quiz()
