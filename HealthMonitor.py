Initialize riskScore = 0
Input bloodSugar, bloodPressure, BMI, cholesterol
For each parameter in (bloodSugar, bloodPressure, BMI, cholesterol)
    If parameter > normal threshold
        Increment riskScore by 1
    Else
        Do nothing
End For
If riskScore >= 3
    Display "High Risk"
Else If riskScore = 2
    Display "Medium Risk"
Else
    Display "Low Risk"
End If
