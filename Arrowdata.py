## TO DO: Make no answer revert to defaults even if converted to float.


def arrow(Vanes = 4, VaneW = 2.3, NockW = 11.5, PointW = 120, InsertW = 20, BowLb = 40, GrainPIn = 0, Inch = 0, BalanceP = 0):

    """
    This Function calculates the weight of the arrow and the FOC if balance point is provided
    """
    print("")
    print("Calculates arrow weight, grains per pound and FOC based on provided Arrow data.")
    print("Default values are within parentheses. Please change to your arrow's measures.")
    print("")
    Inch = input("Arrow length Inches (Obligatory): ") or "0"
    GrainPIn = input("Grains per Inch (Obligatory): ") or "0"
    Vanes = input("Nr of vanes (4): ") or "4"
    VaneW = input("Vane weight (2.3 Grains): ") or "2.3"
    NockW = input("Nock weight (11.5 Grains): ") or "11.5"
    PointW = input("Point weight (125 Grains): ") or "125"
    InsertW = input("Insert weight (20 Grains): ") or "20"
    ExtraW = input("Extra weights (0 Grains): ") or "0"
    BowLb = input("Bow poundage (40 lb): ") or "40"
    BalanceP = input("Balance point (inches from notch grove): ") or "0"

    tofile = input("Do you want to save the data in a file (y/N)?: ")

    GrainPIn = float(GrainPIn)
    Inch = float(Inch)
    Vanes = float(Vanes)
    VaneW = float(VaneW)
    NockW = float(NockW)
    PointW = float(PointW)
    InsertW = float(InsertW)
    ExtraW = float(ExtraW)
    BowLb = float(BowLb)
    BalanceP = float(BalanceP)

    # This is to be un commented when we looked up how to print. Also se the end of file.
    """
    if tofile in ["y", "yes", "Yes", "Y"]:
        pri = input("Do you want to print the file (y/N)?: ")
    """

    Swe = "not possible to calculate without grains per inch."
    Bal = "not possible to calculate with out the Balance Point"
    Agr = "Not possible to calculate without Grain per Inch."

    while Inch == 0:  # or GrainPIn = 0
        # if Inch == 0:
        print("You much provide a value for Inch")
        Inch = int(input("Arrow length (Obligatory): "))

        """
        if GrainPIn == 0:
            print("You much provide a value for Grains per inch")
            GrainPIn = float(input("Grains per Inch (Obligatory): "))
        """

    if BalanceP == 0 and GrainPIn != 0:
        Swe = GrainPIn * Inch + Vanes * VaneW + NockW + PointW + InsertW + ExtraW
        Agr = Swe / BowLb
        # Agr=$(( $Swe / $BowLB ))
        print("The Arrow weight is %d Gr" % Swe)
        print("There are %d Grains per Pound" % Agr)
        print("FOC is %s" % Bal)

    elif GrainPIn == 0 and BalanceP != 0:
        Bal = ((BalanceP - (Inch / 2)) / Inch) * 100
        print("FOC is %d" % Bal)
        print("The Arrow weight and Grains per Pound cannot be calculated without a value of Grains per inch.")
    else:

        if BalanceP != 0 and GrainPIn != 0:
            Swe = GrainPIn * Inch + Vanes * VaneW + NockW + PointW + InsertW + ExtraW
            # Swe=$(( ($GrainPIn * $Inch) + ($Vanes * $VaneW) + ($NockW + $PointW + $InsertW + $ExtraW) ))
            Agr = Swe / BowLb
            Bal = ((BalanceP - (Inch / 2)) / Inch) * 100
            # Bal=$(( ($BalanceP - ($Inch / 2)) / $Inch * 100 ))
            print("The Arrow weight is %d" % Swe)
            print("There are %d Grains per Pound" % Agr)
            print("FOC is %d" % Bal)

        else:
            print("Both Balance point and Grains per inch cannot have value zero!")
            print("Set the correct values for one of them.")
            arrow()

    if tofile in ("y", "Y", "Yes", "yes"):
        with open("Arrowdata", "w") as file:
            file.write("The Arrow weight is {0} \n" "There are {1} Grains per Pound \n" "FOC is {2} \n".format(Swe, Agr, Bal))

        print("The results are saved in the file, Arrowdata")

        """
        if pri in ["y", "Y", "Yes", "yes"]:
            "$HOME/Arrowdata.txt"
            print("The file have also been printed on your default printer.")
        """