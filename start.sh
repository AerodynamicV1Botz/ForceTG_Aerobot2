if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/AerodynamicV1Botz/ForceTG_Aerobot2.0.git /EvaMaria
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /ForceTG_Aerobot2.0
fi
cd /ForceTG_Aerobot2.0
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
