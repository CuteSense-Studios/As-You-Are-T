# Splash screen
label splashscreen:
    scene bg_1 
    pause(2.5)
    hide bg_1
    with fade
return

# ---------------------------------------------------------- (Prologue) --------------------------------------------------------------- #

label start:
    stop music fadeout 1.5 
    scene bg_1
    play sound sfx_1   
    pause 3.0 
    stop sound fadeout 1.0
    "{i}Introductory narration line 1.{/i}"
    "{i}Introductory narration line 2.{/i}"
    "{i}Contextual setup for the current situation.{/i}"
    pause 1.5 
    "{i}Action description leading to the first choice.{/i}"
    with dissolve 
    scene bg_1 
    "{i}Observation regarding the current state.{/i}"                
    play sound sfx_1
    pause 1.0 
    "{i}Internal monologue or realization.{/i}"
    "{i}Further reflection on past events.{/i}"
    "{i}Emotional response to reflections.{/i}"
    "{i}Transition back to the present moment.{/i}"
    pause 1.0 
    "{i}Prompting the player to make the first decision.{/i}"

    menu:
        "Choice Option A (Proactive)": 
            jump branch_a               
        "Choice Option B (Passive)": 
            jump branch_b

label branch_a:
    scene bg_1
    "{i}Resolution narration for picking Option A.{/i}" 
    jump converge_point_1

label branch_b: 
    scene bg_1
    "{i}Resolution narration for picking Option B.{/i}"
    "{i}Secondary thought prompting action anyway.{/i}"
    pause 2.0 
    jump converge_point_2

label converge_point_2:                                                              
    scene bg_1
    "{i}Alternative transition text leading to the same node.{/i}"
    "{i}Further contemplation.{/i}"
    pause 1.0
    jump converge_point_1

label converge_point_1:
    scene bg_1
    "{i}Arrival at the next key location.{/i}"
    pause 1.0 
    with dissolve 
    scene bg_1
    play sound sfx_1
    pause 2.0 
    stop sound fadeout 0.5
    with dissolve 
    scene bg_1 
    play sound sfx_1
    pause 3.5 
    stop sound fadeout 0.5 
    "{i}Description of the new environment.{/i}"
    "{i}Noticing available options or details.{/i}"
    "{i}Focusing on a specific detail.{/i}"
    "{i}Elaborating on the discovered detail.{/i}"
    "{i}Player character reacts to the discovery.{/i}"
    with dissolve 
    scene bg_1 
    play sound sfx_1
    with vpunch 
    pause 2.0 
    "{i}Reading the specific information provided.{/i}"
    "{i}Expressing surprise at the information.{/i}"
    "{i}Formulating a question about the scenario.{/i}"  
    pause 3.5 
    "{i}Hypothesizing reasons for the current situation.{/i}"
    "{i}Deepening curiosity.{/i}"
    "{i}Taking physical action to investigate.{/i}" 
    play sound sfx_1
    with dissolve
    scene bg_1
    "{i}Emotional shift prompting the next decision.{/i}"
    
    menu:
        "Choice Option C (Direct Action)":
            "{i}Committing to the direct action.{/i}"
            jump interaction_scene

        "Choice Option D (Hesitate)":
            "{i}Choosing to delay the action.{/i}"
            "{i}Internal conflict resulting from the delay.{/i}"
            pause 2.5
            "{i}Overcoming hesitation and proceeding anyway.{/i}"
            jump interaction_scene

label interaction_scene: 
    scene bg_1
    play sound sfx_1
    pause 3.0 
    stop sound fadeout 1.0
    "{i}Traveling to the next destination.{/i}"
    with fade 
    scene bg_1
    play sound sfx_1
    pause 4.0 
    stop sound fadeout 1.5 
    "{i}Describing the interior of the new location.{/i}"
    play music music_1
    "{i}Approaching the NPC.{/i}"
    show char_1_idle at zoom_face
    "{i}NPC reaction and physical description.{/i}"
    "{i}Further details about NPC appearance.{/i}"
    "{i}Details about NPC attire.{/i}"
    stop music fadeout 2.0 

    menu: 
        "Dialogue Topic 1 (Specific)": 
            play music music_1 volume 0.4
            "{i}Player asks the specific question.{/i}"
            c1 "NPC provides relevant exposition part 1." 
            c1 "NPC provides relevant exposition part 2."
            c1 "NPC concludes their explanation."
            "{i}Observation of NPC's reaction.{/i}"
            "{i}NPC recovers composure.{/i}"
            "{i}Player states their intention.{/i}"
            c1 "NPC expresses surprise."
            c1 "NPC offers assistance."
            "{i}Player observes NPC's willingness to help.{/i}"
            "{i}Internal feeling of hope.{/i}"
            stop music fadeout 1.0
            with fade 
            jump final_decision
            
        "Dialogue Topic 2 (General)": 
            play music music_1 volume 0.4
            "{i}Player asks a general question.{/i}"
            c1 "NPC provides general worldbuilding part 1."
            c1 "NPC provides general worldbuilding part 2."
            c1 "NPC provides general worldbuilding part 3."
            "{i}Player listens but remains focused on the main goal.{/i}"
            "{i}Player steers the conversation back to the specific topic.{/i}"
            c1 "NPC reacts to the topic change." 
            "{i}NPC demeanor shifts.{/i}"
            c1 "NPC provides background lore part 1."
            c1 "NPC provides background lore part 2."
            c1 "NPC provides background lore part 3."
            "{i}Observation of NPC's emotional state.{/i}"
            "{i}Player states their intention despite the warnings.{/i}"
            c1 "NPC expresses surprise and relief."
            "{i}Observation of NPC's reaction.{/i}"
            stop music fadeout 1.0
            with fade 
            jump final_decision

label final_decision:
    scene bg_1
    "{i}Transition into the final confirmation phase.{/i}"
    c1 "NPC asks for final confirmation."
    
    menu: 
        "Confirm Decision": 
            "{i}Player confirms their choice.{/i}"
            c1 "NPC agrees to process the request."
            scene bg_1
            "{i}Narration of paperwork and formalities.{/i}"
            "{i}Player signs their name.{/i}"
            play sound sfx_1
            pause 2.0 
            play sound sfx_1
            "{i}Emotional payoff of the decision.{/i}"
            scene bg_1
            show char_1_idle at zoom_face
            c1 "NPC brings up a logistical hurdle."
            "{i}Observation of NPC's awkwardness.{/i}"
            "{i}Player reassures the NPC.{/i}"
            c1 "NPC moves past the hurdle."
            "{i}NPC expresses relief.{/i}"
            scene bg_1
            play sound sfx_1
            "{i}Player resolves the logistical hurdle.{/i}"
            pause 2.0 
            play sound sfx_1
            pause 2.0 
            "{i}Player makes a creative decision regarding the transaction.{/i}" 
            "{i}NPC agrees with the creative decision.{/i}"
            play sound sfx_1
            "{i}Player finalizes the creative decision.{/i}"
            pause 2.0
            play sound sfx_1
            play sound sfx_1
            with fade 
            jump chapter_end

        "Reconsider Decision":
            "{i}Player expresses hesitation.{/i}"
            c1 "NPC accepts the hesitation."
            play music music_1
            "{i}Player reflects on the negative alternative.{/i}"
            "{i}Memory of past hardships 1.{/i}"
            "{i}Memory of past hardships 2.{/i}"
            "{i}Memory of past hardships 3.{/i}"
            "{i}Physical reaction to the memories.{/i}"
            stop music fadeout 1.5
            with vpunch 
            play sound sfx_1
            "{i}Overwhelming negative emotion forces a choice.{/i}"
            "{i}Player realizes they must proceed.{/i}"
            play sound sfx_1
            c1 "NPC agrees to process the request."
            scene bg_1
            "{i}Narration of paperwork and formalities.{/i}"
            "{i}Player signs their name.{/i}"
            play sound sfx_1
            pause 2.0 
            play sound sfx_1
            "{i}Emotional payoff of the decision.{/i}"
            scene bg_1
            show char_1_idle at zoom_face
            c1 "NPC brings up a logistical hurdle."
            "{i}Observation of NPC's awkwardness.{/i}"
            "{i}Player reassures the NPC.{/i}"
            c1 "NPC moves past the hurdle."
            "{i}NPC expresses relief.{/i}"
            scene bg_1
            play sound sfx_1
            "{i}Player resolves the logistical hurdle.{/i}"
            pause 2.0 
            play sound sfx_1
            pause 2.0 
            "{i}Player makes a creative decision regarding the transaction.{/i}" 
            "{i}NPC agrees with the creative decision.{/i}"
            play sound sfx_1
            "{i}Player finalizes the creative decision.{/i}"
            pause 2.0
            play sound sfx_1
            play sound sfx_1
            with fade 
            jump chapter_end
    
label chapter_end: 
    scene bg_1
    show char_1_idle at zoom_face
    "{b}{i}Concluding positive emotional statement.{/i}{/b}" 
    "{i}NPC reaction to the completed transaction.{/i}"
    "{i}Player says goodbye.{/i}"
    pause 1.5 
    with fade 
    scene bg_1
    pause 3.0
    play music music_1 volume 0.75
    play sound sfx_1
    "{i}Narration of the journey home.{/i}"
    "{i}Lingering question about the interaction.{/i}"
    pause 1.0
    stop music fadeout 1.0 
    play sound sfx_1
    "{b}{i}Dismissal of the question in favor of rest.{/i}{/b}"
    pause 2.9 
    stop sound
    with fade 
    scene bg_1 
    play sound sfx_1
    "{i}Arrival at the home location.{/i}"
    pause 1.0 
    stop sound 
    play sound sfx_1
    pause 1.5 
    with fade
    scene bg_1 
    "{i}Final narration before sleep.{/i}"
    "{i}Anticipation of the next day's events.{/i}"
    scene bg_1 
    pause 1.0 
    jump day_1

# --------------------------------------------------------(Day 1)-------------------------------------------------------------#
label day_1: 




# PAST