# Get the data for this experiment

# Get POS tagging data
TRAINURL=https://www.clips.uantwerpen.be/conll2000/chunking/train.txt.gz
TRAINZIP=train.txt.gz
TRAINFILE=train.txt

TESTURL=https://www.clips.uantwerpen.be/conll2000/chunking/test.txt.gz
TESTZIP=test.txt.gz
TESTFILE=test.txt

mkdir -p POS
cd POS

if [ ! -e $TRAINFILE ]; then
    if [ ! -e $TRAINZIP ]; then
        wget --quiet --continue $TRAINURL
    fi
    gunzip $TRAINZIP
fi

if [ ! -e $TESTFILE ]; then
    if [ ! -e $TESTZIP ]; then
        wget --quiet --continue $TESTURL
    fi
    gunzip $TESTZIP
fi

# Get ATIS data
cd ..
mkdir -p ATIS
cd ATIS

TRAINURL=https://raw.githubusercontent.com/yvchen/JointSLU/master/data/atis.train.w-intent.iob
TRAINFILE=atis.train.w-intent.iob
TRAIN2URL=https://raw.githubusercontent.com/yvchen/JointSLU/master/data/atis-2.train.w-intent.iob
TRAIN2FILE=atis-2.train.w-intent.iob

DEVURL=https://raw.githubusercontent.com/yvchen/JointSLU/master/data/atis-2.dev.w-intent.iob
DEVFILE=atis-2.dev.w-intent.iob

TESTURL=https://raw.githubusercontent.com/yvchen/JointSLU/master/data/atis.test.w-intent.iob
TESTFILE=atis.test.w-intent.iob

if [ ! -e $TRAINFILE -o ! -e $TRAIN2FILE -o ! -e $DEVFILE -o ! -e $TESTFILE ]; then
    wget --quiet --continue $TRAINURL
    wget --quiet --continue $TRAIN2URL
    wget --quiet --continue $DEVURL
    wget --quiet --continue $TESTURL
fi

python ../../preprocess_atis.py
