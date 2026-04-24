from EmotionDetection import emotion_detector

def test_case(statement, expected_emotion):
    result = emotion_detector(statement)
    actual_emotion = result["dominant_emotion"]
    
    print(f"Statement: {statement}")
    print(f"Expected: {expected_emotion}, Got: {actual_emotion}")
    
    if actual_emotion == expected_emotion:
        print("✅ Test Passed\n")
    else:
        print("❌ Test Failed\n")


# Test cases
test_case("I am glad this happened", "joy")
test_case("I am really mad about this", "anger")
test_case("I feel disgusted just hearing about this", "disgust")
test_case("I am so sad about this", "sadness")
test_case("I am really afraid that this will happen", "fear")