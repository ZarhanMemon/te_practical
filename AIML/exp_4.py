# Forward and backward chaining 


facts = {"raining" }


rules = [
        ({"raining"} , "wet_ground"),
        ({"wet_ground"} , "no_school")
    ]



def forward_chaining ( facts , rules):
    
    known = set(facts)
    
    changed = True
    
    
    while changed:
        
        changed = False
        
        for condition , conclusion in rules:
            if condition <= known and conclusion not in known:
                known.add(conclusion)
                changed = True
                print(f"{condition} => {conclusion}")
    
    return known


print("Forward Chaining:")
result = forward_chaining(facts, rules)
print("Known facts after forward chaining:", result)


#====================================


def backward_chaining( goal , facts , rules):
    
    if goal in facts:
        return True
    
    
    
    return any(
        conclusion == goal 
        and all( 
                backward_chaining( condition , facts , rules) 
                for condition in conditions 
                ) 
        for conditions , conclusion in rules
    )
    
    
    
print("\nBackward Chaining:")

result = backward_chaining("no_school" , facts ,rules)

print(f"Can we derive '{'no_school'}'?: {result}")