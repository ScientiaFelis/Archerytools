#!/bin/bash

###This Function calculates the weight of the arrow and the FOC if balance point is provided##
echo ""
echo "Calculates arrow weight, grains per pound and FOC based on provided Arrow data."
echo "Default values are within parentesis. Plean change to your arrow's measures."
echo ""
read -p "Arrow length (Obligatory): " Inch
read -p "Grains per Inch (Obligatory): " GrainPIn
read -p "Nr of vanes (4): " Vanes
read -p "Vane weight (2.3 Grains): " VaneW
read -p "Nock weight (11.5 Gr): " NockW
read -p "Point weight (125 Gr): " PointW
read -p "Insert weight (20 Gr): " InsertW
read -p "Extra weights (0 Gr): " ExtraW
read -p "Bow poundage (40 lb): " BowLB
read -p "Balance point (inches from noch grove): " BalanceP

read -p "Do you want to save the data in a file (y/N)?: " ToFile

if [[ $ToFile == "y" ]]; then
   read -p "Do you want to print the file (y/N)?: " Pri
fi

Inch=${Inch:=0}
BowLB=${BowLB:=40}
BalanceP=${BalanceP:=0}
GrainPIn=${GrainPIn:=0}

Vanes=${Vanes:=4}
VaneW=${VaneW:=2.3}
NockW=${NockW:=11.5}
PointW=${PointW:=125}
InsertW=${InsertW:=20}
ExtraW=${ExtraW:=0}

Swe=${Swe:="not possible to calculate without grains per inch."}
Bal=${Bal:="not possible to calculate with out the Balance Point"}

echo ""
echo ""
echo ""

  if [[ $Inch == 0 ]]; then
     echo "You much provide a value for Inch"
     read -p "Arrow length in inches: " Inch
 fi

 if [[ $GrainPIn == 0 ]]; then
    echo "You much provide a value for Grains per inch"
    read -p "Grains per Inch: " GrainPIn
fi

clear
echo ""

if [[ $BalanceP == 0 && $GrainPIn != 0 ]];then
      Swe=$( echo "scale=3;($GrainPIn * $Inch) + ($Vanes * $VaneW) + ($NockW + $PointW + $InsertW + $ExtraW)" | bc)
      Agr=$( echo "scale=3;$Swe / $BowLB" | bc)
      #Agr=$(( $Swe / $BowLB ))
      echo -e "The Arrow weight is ${Swe} Gr \n"
      echo -e "There are ${Agr} Grains per Pound \n"
       echo -e "FOC is ${Bal} \n"

 elif [[  $GrainPIn == 0 && $BalanceP != 0 ]]; then
          Bal=$( echo "scale=3;($BalanceP - ($Inch/2)) /$Inch * 100" | bc)
          echo -e "FOC is ${Bal} \n"
          echo -e "The Arrow weight and Grains per Pound cannot be calculated without a value of Grains per inch. \n"
else

      if [[ $BalanceP != 0 && $GrainPIn != 0 ]]; then
         Swe=$( echo "scale=3;($GrainPIn * $Inch) + ($Vanes * $VaneW) + ($NockW + $PointW + $InsertW + $ExtraW)" | bc)
            #Swe=$(( ($GrainPIn * $Inch) + ($Vanes * $VaneW) + ($NockW + $PointW + $InsertW + $ExtraW) ))
            Agr=$(echo "scale=3;$Swe / $BowLB" | bc)
            Bal=$(echo "scale=3;($BalanceP - ($Inch / 2)) / $Inch * 100" | bc)
            #Bal=$(( ($BalanceP - ($Inch / 2)) / $Inch * 100 ))
            echo -e "The Arrow weight is ${Swe} \n"
            echo -e "There are ${Agr} Grains per Pound \n"
            echo -e "FOC is ${Bal} \n"

      else
          echo "Both Balance point and Grains per inch cannot have cero value."
          echo "Set the correct values for one of them."
          exit
      fi

fi

if [[ $ToFile == "y" ]]; then

   echo -e "The Arrow weight is ${Swe} \n" "There are ${Agr} Grains per Pound \n" "FOC is ${Bal} \n" > "$HOME/Arrowdata.txt"
   echo ""
    echo "The results are saved in the file, Arrowdata.txt, in your HOME directory"

   if [[ $Pri == "y" ]]; then
      lp "$HOME/Arrowdata.txt"
      echo "The file have also been printed on your default printer."
   fi

fi
