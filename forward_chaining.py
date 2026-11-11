
# AI LAB: FIRST ORDER LOGIC USING FORWARD CHAINING

facts = set()
rules = []


# ----------------------------------
# STEP 1: PROCESS ENGLISH SENTENCES
# ----------------------------------

def process_sentence(sentence):

    s = sentence.lower().strip().rstrip(".")

    # Rule: Americans selling weapons to hostile nations
    # are criminals

    if "crime" in s and "american" in s and "weapon" in s:

        rules.append((
            [
                ("American", "?x"),
                ("Weapon", "?y"),
                ("Sells", "?x", "?y", "?z"),
                ("Hostile", "?z")
            ],
            ("Criminal", "?x")
        ))

    # Country A is an enemy of America

    elif "enemy" in s and "america" in s:

        facts.add(("Enemy", "CountryA", "America"))
        facts.add(("Hostile", "CountryA"))
        facts.add(("Missile", "M1"))

    # All missiles are weapons

    elif "all missiles are weapons" in s:

        rules.append((
            [("Missile", "?x")],
            ("Weapon", "?x")
        ))

    # Robert sold missiles to Country A
    # Robert is an American citizen

    elif "robert" in s and "sold" in s and "missile" in s:

        facts.add(("Sells", "Robert", "M1", "CountryA"))
        facts.add(("American", "Robert"))

    else:
        print("Sentence not recognized:", sentence)


# ----------------------------------
# STEP 2: UNIFICATION
# ----------------------------------

def unify(pattern, fact, substitution):

    if len(pattern) != len(fact):
        return None

    if pattern[0] != fact[0]:
        return None

    sub = substitution.copy()

    for p, f in zip(pattern[1:], fact[1:]):

        if p.startswith("?"):

            if p in sub and sub[p] != f:
                return None

            sub[p] = f

        elif p != f:
            return None

    return sub


# ----------------------------------
# STEP 3: MATCH RULE CONDITIONS
# ----------------------------------

def match_conditions(conditions, known_facts, sub=None):

    if sub is None:
        sub = {}

    if not conditions:
        return [sub]

    results = []

    first = conditions[0]

    for fact in known_facts:

        new_sub = unify(first, fact, sub)

        if new_sub is not None:

            results.extend(
                match_conditions(
                    conditions[1:],
                    known_facts,
                    new_sub
                )
            )

    return results


# ----------------------------------
# STEP 4: APPLY SUBSTITUTION
# ----------------------------------

def apply_substitution(expression, sub):

    return tuple(
        sub.get(item, item) if item.startswith("?") else item
        for item in expression
    )


# ----------------------------------
# STEP 5: FORWARD CHAINING
# ----------------------------------

def forward_chaining(query):

    while True:

        new_facts = set()

        for conditions, conclusion in rules:

            substitutions = match_conditions(
                conditions, list(facts)
            )

            for sub in substitutions:

                new_fact = apply_substitution(
                    conclusion, sub
                )

                if new_fact not in facts:
                    new_facts.add(new_fact)

        if query in new_facts:

            facts.update(new_facts)

            print("\nNew facts derived:")

            for fact in sorted(new_facts):
                print(fact)

            return True

        if not new_facts:
            return query in facts

        print("\nNew facts derived:")

        for fact in sorted(new_facts):
            print(fact)

        facts.update(new_facts)


# ----------------------------------
# STEP 6: MAIN PROGRAM
# ----------------------------------

print("KNOWLEDGE BASE USING FIRST ORDER LOGIC")
print("--------------------------------------")

n = int(input("\nEnter number of sentences: "))

for i in range(n):

    sentence = input("Enter sentence " + str(i + 1) + ": ")

    process_sentence(sentence)


# DISPLAY KNOWLEDGE BASE

print("\n----------- KNOWLEDGE BASE -----------")

print("\nFacts:")

for fact in sorted(facts):
    print(fact)

print("\nRules:")

for conditions, conclusion in rules:
    print(conditions, "->", conclusion)


# ----------------------------------
# STEP 7: USER QUERY
# ----------------------------------

print("\n----------- ENTER QUERY -----------")

query_name = input("Enter person name: ").strip().title()

query_predicate = input("Enter predicate: ").strip().capitalize()

query = (query_predicate, query_name)


# ----------------------------------
# STEP 8: FORWARD REASONING
# ----------------------------------

print("\n----------- FORWARD REASONING -----------")

if forward_chaining(query):

    print("\nQUERY PROVED: TRUE")
    print(query_name, "is", query_predicate.lower())

else:

    print("\nQUERY NOT PROVED: FALSE")
    print(query_name, "is not proved to be", query_predicate.lower())
