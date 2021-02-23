# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholesterol = 70
low_cholesterol = total_cholesterol < 200
medium_cholesterol = 200 < total_cholesterol < 240
high_cholesterol = 200 < total_cholesterol > 240

ldl = 30
low_ldl = ldl < 100
medium_ldl = 130 < ldl < 160
high_ldl = ldl > 160

triglyceride = 120
low_triglyceride = triglyceride < 150
medium_triglyceride = 150 <= triglyceride < 200
high_triglyceride = triglyceride >= 200

# if total_cholesterol < 200 and ldl < 100 and triglyceride < 150:
if low_cholesterol and low_ldl and low_triglyceride:
    # good level
    print('*** Good level of cholestrol ***')
# elif 200 < total_cholesterol > 240 or ldl > 160 or triglyceride >= 200:
elif high_cholesterol or high_ldl or high_triglyceride:
    # High cholestrol level
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
# elif 200 <total_cholesterol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200:
elif medium_cholesterol or medium_ldl or medium_triglyceride:
    # TLC_diet
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
else:
    print('Error: unhandled case.')
