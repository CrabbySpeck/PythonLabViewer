while true; do
    read -p "What file do you want to track?" yn
    git add $yn; break;
done
