!/usr/bin/python -tt
import sys
import twitterwtfrecommender 

def __show_usage():
    print "Following is the correct usage:"
    print "./twitter_recommender <inputFile.json> <aggressiveness Factor> <outputFile.json>"
    exit(1)

def main():
    #Validate command line arguments
    if len(sys.argv) != 4:
        print "Incorrect Number of arguments"
        __show_usage()
    inputFile = sys.argv[1]
    aggFactor = sys.argv[2]
    outputFile = sys.argv[3]
    print "Started WTF recommendation for twitter..."
    recObj = twitterwtfrecommender.TwitterWTFRecommender()
    status = recObj.generateWTFReco(inputFile, aggFactor, outputFile)
    if status != 0:
        print "Failed while creating WTF recommendations"
        exit(1)
    else:
        print 'Successfully completed  WTF twitter recommendation'
if __name__ == "__main__":
    main()
