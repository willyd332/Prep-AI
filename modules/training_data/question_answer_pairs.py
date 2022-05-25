# Q&A Pairs for question answering model. In the future this can be more refined






cold_war_context = '''
This was the way the war was supposed to end: with cheers, handshakes, dancing, drinking, and hope. The date was April 25, 1945, the place the eastern German city of Torgau on the Elbe, the event the first meeting of the armies, converging from opposite ends of the earth, that had cut Nazi Germany in two. Five days later Adolf Hitler blew his brains out beneath the rubble that was all that was left of Berlin. Just over a week after that, the Germans surrendered unconditionally. The leaders of the victorious Grand Alliance, Franklin D. Roosevelt, Winston Churchill, and Josef Stalin, had already exchanged their own handshakes, toasts, and hopes for a better world at two wartime  summits—Teheran in November, 1943, and Yalta in February, 1945. These gestures would have meant little, though, had the troops they commanded not been able to stage their own more boisterous celebration where it really counted: on the front lines of a battlefield from which the enemy was now disappearing.
Why, then, did the armies at Torgau approach one another warily, as if they'd been expecting interplanetary visitors? Why did the resemblances they saw seem so surprising—and so reassuring? Why, despite these, did their commanders insist on separate surrender ceremonies, one for the western front at Reims, in France, on May 7th, another for the eastern front in Berlin on May 8th? Why did the Soviet authorities try to break up spontaneous pro-American demonstrations that erupted in Moscow following the official announcement of the German capitulation? Why did the American authorities, during the week that followed, abruptly suspend critical shipments of Lend-Lease aid to the U.S.S.R., and then resume them? Why did Roosevelt's key aide Harry Hopkins, who had played a decisive role in crafting the Grand Alliance in 1941, have to rush to Moscow six weeks after his boss's death to try to save it? Why for that matter, years later, would Churchill title his memoir of these events Triumph and Tragedy?
The answer to all of these questions is much the same: that the war had been won by a coalition whose principal members were already at war—ideologically and geopolitically if not militarily—with one another. Whatever the Grand Alliance's triumphs in the spring of 1945, its success had always depended upon the pursuit of compatible objectives by incompatible systems. The tragedy was this: that victory would require the victors either to cease to be who they were, or to give up much of what they had hoped, by fighting the war, to attain.
'''

cold_war_QA_pairs = [
    [
      "What were the causes of the Cold War?",
      '''
      The true beginning of the Cold War is difficult to pin down. Despite the alliance between the US and the USSR during WWII, the two powers' ideological and geopolitical interests were not aligned. In Hitler's Fascism, they found a mutual enemy, but the gap between a Democratic, Capitalist West and an Authoritarian, Communist East could not be closed so easily. At the Yalta Conference in 1945, the leaders of Britain (Churchill), the US (Roosevelt), and the Soviet Union (Stalin) agreed that, after Germany's defeat, most of Eastern Europe would be controlled by the Soviets. That summer, then with President Truman leading the US, a defeated Germany and Berlin were partitioned into three Western sections and a Soviet section. At the same time, the US established itself as the sole controller and occupier of a defeated Japan.
	    '''
    ]
]




#### More Examples


general_QA_pairs = [
    [
      "What is the theoretical foundation of the Stability-Instability Paradox?",
      "The theoretical foundation of the Stability-Instability Paradox (S-I Paradox) comes from Glenn Snyder's seminal 1960 paper, Balance of Power in the Missile Age. In it, the author explains how nuclear weapons cause an shift away from a traditional balance of power dynamics in international relations, and instead bring about a “balance of terror,” where states seek to deter opponents with the threat of nuclear punishment. Among other theoretical implications of nuclear weapons, the author explains the core idea of the S-I Paradox: 'when the strategic balance is stable, when both sides have the capacity to strike back powerfully after absorbing a first strike, the tactical balance tends to become unstable because limited attacks can be undertaken and limited wars can be carried to fairly high levels of intensity without serious danger that either side will decide to initiate all-out strategic warfare.'"
    ],
    [
      "What do you think of the term 'orientalism' as far as it relates to European arts depicting perceptions of life in the Ottoman Empire? In your response, consider our discussion of the Ottoman Empire in general, as wel as some of the paintings in the slide-presentation we saw.",
      "One thing that stands out is that 'Oriental' wasn't depicted as explicitly negative. Often these paintings are quite beautiful and show grand cities and halls. However, they are also clearly trying to highlight some fundamental differences between the Ottomans and the West. There are certainly some common motifs in the paintings. One I notice is the depiction of the Hookah, which appears throughout Jean Léon Gérome's paintings. To me it seems as though he's saying 'look how different this is from how we smoke!' Another of Gérome's motifs is the depiction of Ottoman Harems and slavery. I notice that the women depicted as slaves in the Harem are usually depicted to look more European than other figures (see 'The Bath' and 'The Harem Pool'). Finally, I want to point out Gérome's depictions of daily life for the Ottomans. He depicts street vendors, animals, people going to pray, slave markets, and serpent charmers. While they are mad to seem mundane in their context, they are meant to be fascinating and unique to the European audience. In Delacroix's paintings, the Ottomans are depicted differently. Where Gérome often focuses on the daily life of Ottoman people, Delacroix focuses frequently on violent scenes. Often they are incredibly brutal, like 'Death of Sardanapalus'  or 'Arabs Skirmishing in the Mountains.' There are also some paintings depicting Napoleon during his encounters in the Middle East, like Gros's 'Napoleon in the Pest House at Jaffa.'"
    ],
    [
      "How well is the solution described, is it unique and better than existing solutions, how well does it address the outlined problem, and what is it worth to those experiencing the problem?  To what extent is the invention ready for commercial adoption, where does it fall on the idea-to-product continuum?",
      '''
      The solution describes a novel process of E. coli directed evolution using the AIDE method. Initially, the researchers plan to slave the well-defined problem of non-secreting E. coli to reduce insulin costs. To accomplish this, they utilize the p1 Phage virus which has a genome size of about 90,000 pairs. Using a mutated phagemid with the desired genes packaged within the P1, they infect E. coli cells. They then filter out the high performing (high secreting) cells, extract their genes, generate further mutations, and repeat the process.
      This process has been proven before by engineering E. coli via evolution to consume tagatose. However, it has not been proven for a proinsulin solution specifically. The key to this process is that the secretion network of E. Coli is 20,000 base pairs, and so the novel AIDE method is the only method that can effectively target this system because it is theoretically able to handle up to 90,000 base pair mutations. Once confirmed, the novel strain of E. coli will be quickly ready for commercial adoption as many insulin producers already utilize different E. coli strains. Additionally, success in this proinsulin secreting endeavor would prove that AIDE itself is useful for industrial production.
      '''
    ]
  ]


history_QA_pairs = [
    [
      "Why did Napoleon incorporate the Illyrian Provinces into the French Empire?",
      "The were multiple, overlapping and sometimes contradictory imperatives at work when Napoleon created the Illyrian Provinces in 1809. The main rationale for Napoleon was that the Illyrian Provinces would strengthen the Continental System by putting a large swath of the Adriatic under direct French control. This would strengthen the blockade and end smuggling. Napoleon operated under the general logic that Austria had proven susceptible to British influence and that by eliminating her outlet to the sea, France could gain a more pliant ally on the continent. The French strategic rationale was also that they could create a buffer state in the Balkans on the flank of Southeastern Europe which would act analogous to the Duchy of Warsaw. They would be a direct source for manpower and revenue for French interests in this region of Europe. The erection of the Illyrian Provinces was also of a piece with Napoleon's various annexations of other territories like Holland and the Papal States. Unlike other voices within the French government, Napoleon conceived of citizenship as jus sli (from the soil) in which Frenchmen could be made through acculturation to French norms and values. So the Illyrian Provinces fit within Napoleon's conception of the universal French empire he was creating."
    ],
    [
      "How did the development of agriculture affect plant evolution?",
      '''
      The development of agriculture created ecological niches where humans sought to eliminate all but a small selection of useful species. In this way, garden were 'Open Habitats' that created ecological space for mutations that never would have been able to survive normally.
      The author gives a few examples of this on the third full paragraph on page 185: 'In fact, a lot of new things happen in the garden...'
      This is especially true for new traits that are desirable to humans and could be artificially selected for. The author describes artificial selection as an 'ongoing back and forth between the land and its cultivators,' because while mutations happened naturally, it was the humans who cultivated certain traits above others. More recently, with the development of technology that allows us to genetically modify cells directly, this process has been accelerated. The author hints at the idea that, although artificial, GMOs (and agriculture) should still be considered a part of evolution, as plants and animals co-evolve together.
      '''
    ],
    [
      "Why did the Cold War finally end?",
      '''
      By 1980, the anti-war sentiment in the US was established. Citizens were not only terrified of Soviet nuclear weapons but terrified of nuclear weapons in general and intellectuals like Carl Sagan demonstrated the potentially horrible effects of the weapons. Although the newly elected President Ronald Reagan was initially aggressive towards the Soviets, it was under his Presidency that the relations between the two powers truly started to thaw. By 1985, Mikhail Gorbachev, the new leader of the USSR, could see that the public opinion in the USSR was shifting. Soviets were struggling economically, and the citizens were becoming more and more cynical about communism after the election of Polish Pope John Paul II in 1978 and the Chernobyl Disaster in 1986.
	    Gorbachev decided to shift away from traditional Soviet communism to remedy the situation. Implementing Perestroika (economic reform) and Glasnost (openness) promoting entrepreneurship, Gorbachev struggled to save the USSR, however, Gorbachev was unwilling to use force to do so. In 1987, Reagan gave a speech urging Gorbachev to tear down the Berlin Wall. In 1989, after Gorbachev failed to crack down on the opening of the Hungary-Austrian border, the Iron Curtain was dismantled and the Berlin Wall was taken down. The newly elected President George H. W. Bush began helping the Soviets transition to democracy, but immediately after Boris Yeltsin was elected as the leader of the USSR in 1991 he dismantled the Soviet Union entirely, finally ending a 50-year-old war. Although the effects of the Cold War certainly lingered, the War itself was over.
      '''
    ]
  ]

business_QA_pairs = []