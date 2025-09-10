from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# الصفحة الرئيسية لعرض واجهة المستخدم
@app.route('/')
def home():
    return render_template("home.html")

# صفحة الكشف عن الفيديو والصورة
@app.route('/deepfake-detection')
def deepfake_detection():
    return render_template("deepfake_detection.html")

# نقطة نهاية لمعالجة الفيديو
@app.route('/predictVideo', methods=['POST'])
def predict_video():
    try:
        video = request.files.get('video')
        if not video:
            return jsonify({"message": "No video provided"}), 400

        video_path = "video.mp4"
        video.save(video_path)
        # بدون معالجة الفيديو
        return jsonify({'message': 'Video received and saved successfully'})
    except Exception as e:
        print(e)
        return jsonify({"message": "Error in processing video"}), 500

# نقطة نهاية لمعالجة الصورة
@app.route('/predictImage', methods=['POST'])
def predict_image():
    try:
        image = request.files.get('image')
        if not image:
            return jsonify({"message": "No image provided"}), 400

        image_path = "image.jpg"
        image.save(image_path)
        # بدون معالجة الصورة
        return jsonify({'message': 'Image received and saved successfully'})
    except Exception as e:
        print(e)
        return jsonify({"message": "Error in processing image"}), 500

# نقاط النهاية الأخرى (مثل about و contact) يمكن إضافتها هنا إذا كنت بحاجة إليها
@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
