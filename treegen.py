# the goal is to make a program start starts with an upp and lower limit and
#increments from the start to finish in a certain pattern

import cs1graphics as cg

def rightside(hlimlow,hlimhigh,vlimlow,vlimhigh,branches):

    hlist_r=[]
    vlist_r=[]

    #creating a variable to use as the 'increment' which will change with the number of desired branches
    vstep = int((vlimhigh-vlimlow)/branches)
    hstep = int((hlimhigh-hlimlow)/branches)

    #instantiating control variables
    var1 = 1
    var2 = 1

    _ = 0                                                               #creating a loop for special first-case

    for i in range(hlimlow,hlimhigh,hstep):
            if _ == 0:                                                  #creating a loop for special first-case
                #print('hello')                                         #here for testing
                _ += 1
                h_outer_peak    =   round(hlimhigh)                     #first loop is set at the limit
                h_swoop_in      =   round(hlimhigh-(1.3*hstep))          #goes inward by 50% of the step
                h_inner_peak    =   round(hlimhigh-(2.2*hstep))               #goes all the way to the minimum of the step
                h_swoop_out     =   round(hlimhigh-(.5*hstep))          #goes outward again by 40% of the step

                #writing results of this loop to a list
                hlist_r.append(h_outer_peak)
                hlist_r.append(h_swoop_in)
                hlist_r.append(h_inner_peak)
                hlist_r.append(h_swoop_out)
            
            elif var1 == (branches-1):                                  #checking to see if it is the last loop! we don't "swoop" back out for the last loop
                new_hlimhigh    =   hlimhigh-(hstep*var1)               #creating this to update the variable each loop. essentially redefining the new maxima
                #print(i)                                               #here for testing

                h_outer_peak    =   round(new_hlimhigh)                 #once again it is simply the value of the updated variable for hlimhigh
                h_swoop_in      =   round(new_hlimhigh-(.5*hstep))      #same as first loop
                h_inner_peak    =   round(new_hlimhigh-hstep)           #^

                #writing results of this loop to a list
                hlist_r.append(h_outer_peak)
                hlist_r.append(h_swoop_in)
                hlist_r.append(h_inner_peak)
                var1 += 1                                               #incrementing control variable

            else:
                
                new_hlimhigh    =   hlimhigh-(hstep*var1)               #creating this to update the variable each loop. essentially redefining the new maxima

                h_outer_peak    =   round(new_hlimhigh)                 #once again it is simply the value of the updated variable for hlimhigh
                h_swoop_in      =   round(new_hlimhigh-(1.3*hstep))      #same as first loop
                h_inner_peak    =   round(new_hlimhigh-(2.2*hstep))           #^
                h_swoop_out     =   round(new_hlimhigh-(.5*hstep))      #^

                #writing results of this loop to a list
                hlist_r.append(h_outer_peak)
                hlist_r.append(h_swoop_in)
                hlist_r.append(h_inner_peak)
                hlist_r.append(h_swoop_out)
                var1 += 1                                               #incrementing control variable

    _ = 0                                                               #re-initialize variable for next set of loops

    for i in range(vlimlow,vlimhigh,vstep):
            if _ == 0:                                                  #creating a loop for special first-case
                #print('hello again')                                   #here for testing

                _ += 1                                                  #incrementing control variable to prevent loop from running again

                v_outer_peak    =   round(vlimlow)                      #first loop is set at the limit
                v_swoop_in      =   round(vlimlow+(.5*vstep))           #goes upward by 40% of the step
                v_inner_peak    =   round(vlimlow+(vstep))                #goes all the way to the maximum of the step
                v_swoop_out     =   round(vlimlow+(.7*vstep))           #goes back down by 30% of the step

                #writing results of this loop to a list
                vlist_r.append(v_outer_peak)
                vlist_r.append(v_swoop_in)
                vlist_r.append(v_inner_peak)
                vlist_r.append(v_swoop_out)

            elif var2 == (branches-1):
                new_vlimlow     =   vlimlow+(vstep*var2)                #creating this to update the variable each loop. essentially redefining the new maxima
                #print(new_vlimlow)                                     #here for testing

                v_outer_peak    =   round(new_vlimlow-(.1*vstep))       #once again it is simply the value of the updated variable for vlimlow
                v_swoop_in      =   round(new_vlimlow+(.5*vstep))       #same as first loop
                v_inner_peak    =   round(new_vlimlow+vstep)            #^

                #writing results of this loop to a list
                vlist_r.append(v_outer_peak)
                vlist_r.append(v_swoop_in)
                vlist_r.append(v_inner_peak)
                var2 += 1                                               #incrementing control variable
            else:
                
                new_vlimlow     =   vlimlow+(vstep*var2)                #creating this to update the variable each loop. essentially redefining the new maxima
                #print(new_vlimlow)                                     #here for testing

                v_outer_peak    =   round(new_vlimlow-(.1*vstep))       #once again it is simply the value of the updated variable for vlimlow
                v_swoop_in      =   round(new_vlimlow+(.5*vstep))       #same as first loop
                v_inner_peak    =   round(new_vlimlow+vstep)            #^
                v_swoop_out     =   round(new_vlimlow+(.7*vstep))       #^

                #writing results of this loop to a list
                vlist_r.append(v_outer_peak)
                vlist_r.append(v_swoop_in)
                vlist_r.append(v_inner_peak)
                vlist_r.append(v_swoop_out)
                var2 += 1                                               #incrementing control variable
    return(vlist_r,hlist_r)

def leftside(hlimlow,hlimhigh,vlimlow,vlimhigh,branches):



    hlist_l=[]
    vlist_l=[]

    vstep = int((vlimhigh-vlimlow)/branches)
    hstep = int((hlimhigh-hlimlow)/branches)

    distanceleft = (hlimlow-(hlimhigh-hlimlow))
    #print(distanceleft)

    #print(vstep)
    #print(hstep)

    #instantiating control variables
    var1 = 1
    var2 = 1

    _ = 0                                                               #creating a loop for special first-case

    for i in range(distanceleft,hlimlow,hstep):
            if _ == 0:                                                  #creating a loop for special first-case
                #print('hello')                                         #here for testing
                _ += 1
                h_outer_peak    =   round(distanceleft)                     #first loop is set at the limit
                h_swoop_in      =   round(distanceleft+(1.3*hstep))          #goes inward by 50% of the step
                h_inner_peak    =   round(distanceleft+(2.2*hstep))               #goes all the way to the minimum of the step
                h_swoop_out     =   round(distanceleft+(.5*hstep))          #goes outward again by 40% of the step

                #writing results of this loop to a list
                hlist_l.append(h_outer_peak)
                hlist_l.append(h_swoop_in)
                hlist_l.append(h_inner_peak)
                hlist_l.append(h_swoop_out)
            
            elif var1 == (branches-1):                               #checking to see if it is the last loop! we don't "swoop" back out for the last loop
                new_hlimhigh    =   distanceleft+(hstep*var1)               #creating this to update the variable each loop. essentially redefining the new maxima
                #print(i)                                               #here for testing

                h_outer_peak    =   round(new_hlimhigh)                 #once again it is simply the value of the updated variable for hlimhigh
                h_swoop_in      =   round(new_hlimhigh+(.5*hstep))      #same as first loop
                h_inner_peak    =   round(new_hlimhigh+hstep)           #^

                #writing results of this loop to a list
                hlist_l.append(h_outer_peak)
                hlist_l.append(h_swoop_in)
                hlist_l.append(h_inner_peak)
                var1 += 1                                               #incrementing control variable

            else:
                
                new_hlimhigh    =   distanceleft+(hstep*var1)               #creating this to update the variable each loop. essentially redefining the new maxima

                h_outer_peak    =   round(new_hlimhigh)                 #once again it is simply the value of the updated variable for hlimhigh
                h_swoop_in      =   round(new_hlimhigh+(1.3*hstep))      #same as first loop
                h_inner_peak    =   round(new_hlimhigh+(2.2*hstep))           #^
                h_swoop_out     =   round(new_hlimhigh+(.5*hstep))      #^

                #writing results of this loop to a list
                hlist_l.append(h_outer_peak)
                hlist_l.append(h_swoop_in)
                hlist_l.append(h_inner_peak)
                hlist_l.append(h_swoop_out)
                var1 += 1                                               #incrementing control variable

    _ = 0                                                               #re-initialize variable for next set of loops

    for i in range(vlimlow,vlimhigh,vstep):
            if _ == 0:                                                  #creating a loop for special first-case
                #print('hello again')                                   #here for testing

                _ += 1                                                  #incrementing control variable to prevent loop from running again

                v_outer_peak    =   round(vlimlow)                      #first loop is set at the limit
                v_swoop_in      =   round(vlimlow+(.5*vstep))           #goes upward by 40% of the step
                v_inner_peak    =   round(vlimlow+vstep)                #goes all the way to the maximum of the step
                v_swoop_out     =   round(vlimlow+(.7*vstep))           #goes back down by 30% of the step

                #writing results of this loop to a list
                vlist_l.append(v_outer_peak)
                vlist_l.append(v_swoop_in)
                vlist_l.append(v_inner_peak)
                vlist_l.append(v_swoop_out)

            elif var2 == (branches-1):
                new_vlimlow     =   vlimlow+(vstep*var2)                #creating this to update the variable each loop. essentially redefining the new maxima
                #print(new_vlimlow)                                     #here for testing

                v_outer_peak    =   round(new_vlimlow-(.1*vstep))                  #once again it is simply the value of the updated variable for vlimlow
                v_swoop_in      =   round(new_vlimlow+(.5*vstep))       #same as first loop
                v_inner_peak    =   round(new_vlimlow+vstep)            #^

                #writing results of this loop to a list
                vlist_l.append(v_outer_peak)
                vlist_l.append(v_swoop_in)
                vlist_l.append(v_inner_peak)
                var2 += 1                                               #incrementing control variable
            else:
                
                new_vlimlow     =   vlimlow+(vstep*var2)                #creating this to update the variable each loop. essentially redefining the new maxima
                #print(new_vlimlow)                                     #here for testing

                v_outer_peak    =   round(new_vlimlow-(.1*vstep))                  #once again it is simply the value of the updated variable for vlimlow
                v_swoop_in      =   round(new_vlimlow+(.5*vstep))       #same as first loop
                v_inner_peak    =   round(new_vlimlow+vstep)            #^
                v_swoop_out     =   round(new_vlimlow+(.7*vstep))       #^

                #writing results of this loop to a list
                vlist_l.append(v_outer_peak)
                vlist_l.append(v_swoop_in)
                vlist_l.append(v_inner_peak)
                vlist_l.append(v_swoop_out)
                var2 += 1                                               #incrementing control variable
    return(vlist_l,hlist_l)

def maketrees(trees,location=(0,0),hw=(100,25)):
    
    #defining basic points and creating shape

    #center top
    p1=location
    #bottom left
    p2=(location[0]-hw[1]),(location[1]+hw[0])
    #bottom right
    p3=(location[0]+hw[1]),(location[1]+hw[0])
    tree = cg.Polygon(cg.Point(p1[0],p1[1]),cg.Point(p3[0],p3[1]),cg.Point(p2[0],p2[1]))

    #setting full dimensions
    hll     = location[0]
    hlh     = hw[1]
    vll     = location[1]-hw[0]
    vlh     = location[1]
    branch  = int(input('how many branches do you want? '))

    rl =[rightside(hll,hlh,vll,vlh,branch)]
    ll =[leftside(hll,hlh,vll,vlh,branch)]

    leftcoord   =[]
    rightcoord  =[]

    _ = 0
    for i in rl[0][0]:                                                      #just using this index because all of the lists are the same length. any would work
        if -rl[0][0][0+_] > p1[1] and rl[0][1][0+_] > p1[0]:
            coordset    = rl[0][1][0+_],-rl[0][0][0+_]
            rightcoord.append(coordset)
            _+=1
        else:
            break

    _ = 0
    for i in ll[0][0]:
        if -ll[0][0][0+_] > p1[1] and ll[0][1][0+_] < p1[0]:
            coordset = ll[0][1][0+_],-ll[0][0][0+_]
            leftcoord.append(coordset)
            _+=1
        else:
            break

    print(leftcoord)
    print(rightcoord)

    #creating left side
    h=0
    for i in leftcoord:
        #print(leftcoord[h][0],leftcoord[h][1])
        tree.addPoint(cg.Point(leftcoord[h][0],leftcoord[h][1]),1)
        h+=1

    #creating right side
    h=0
    for i in rightcoord:
        #print(rightcoord[h][0],rightcoord[h][1])
        tree.addPoint(cg.Point(rightcoord[h][0],rightcoord[h][1]))
        h+=1

    #cloning
    treelist=[]
    for i in range(0,trees):
        treelist.append(f'tree{i+1}')

    h=0
    for i in treelist:
        treelist[h] = tree.clone()
        #Backdrop.add(treelist[h])
        #print(treelist[h])
        h+=1

    #print(treelist)
    blah = cg.Canvas(750,500)
    for i in range(0,trees):
        blah.add(treelist[i])
        treelist[i].setFillColor('green')
        treelist[i].move(200+(i*30),200+(i*30))

    return(tree,treelist)

def main():
    number_of_trees = int(input('How many Trees do you want? '))
    location        = int(input('What x coordinate do you want the tree tip at? ')),int(input('What y coordinate do you want the tree tip at? '))
    height          = int(input('How tall do you want the tree? '))
    width           = int(input('How wide do you want the tree? '))
    dimensions      = (height),int((width/2)) if width%2==0 else int((width/2)-1)
    print(f'The dimensions of the tree will be: {dimensions}.')

    #maketrees(number_of_trees,location,dimensions)

    #TESTING


    return(maketrees(number_of_trees,location,dimensions))

main()
# hll     = int(input('what is the horizontal lower limit? '))
# hlh     = int(input('what is horizontal higher limit? '))
# vll     = int(input('what is the vertical lower limit? '))
# vlh     = int(input('what is the vertical higher limit? '))
# branch  = int(input('how many branches do you want? '))

# print(rightside(hll,hlh,vll,vlh,branch))
# print(leftside(hll,hlh,vll,vlh,branch))

# rl =[rightside(hll,hlh,vll,vlh,branch)]
# ll =[leftside(hll,hlh,vll,vlh,branch)]

# #making tree
# leftcoord   =[]
# rightcoord  =[]

# _ = 0
# for i in rl[0][0]:                                                      #just using this index because all of the lists are the same length. any would work
#     coordset    = rl[0][1][0+_],rl[0][0][0+_]
#     rightcoord.append(coordset)
#     _+=1

# _ = 0
# for i in ll[0][0]:
#     coordset = ll[0][1][0+_],ll[0][0][0+_]
#     leftcoord.append(coordset)
#     _+=1

# print(leftcoord[0])
# print(rightcoord[0])
