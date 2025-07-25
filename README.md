Diabetic Retinopathy Detection (Scan4Sight)

A deep learning-powered desktop application for automated detection of diabetic retinopathy from retinal images. Integrates a PyTorch-based ResNet model, MySQL user management, a Tkinter graphical user interface, and results notification via SMS.

🚀 Overview:

Scan4Sight is designed to assist clinicians and patients by providing quick, reliable, and accessible screening for diabetic retinopathy (DR). The application allows authenticated users to upload retinal images, receive instantaneous severity classification, and get notified of their results via SMS.

🔥 Features:

   - User Authentication: Signup and Login system using MySQL.

   - Intuitive GUI: Built with Tkinter for easy use by clinicians or patients with minimal technical expertise.

   - End-to-End Prediction: Uploads a retinal image and classifies the severity of diabetic retinopathy into 5 classes.

   - Deep Learning Backbone: Uses a PyTorch ResNet-152-based model for robust DR classification.

   - Automated SMS Notification: Notifies users of prediction results via Twilio.

   - Image Visualization: Displays the analyzed image along with the predicted label and class.

Dataset : APOTS Kaggle Blindness Detection Dataset

🛠️ Tech Stack:

    Programming-	Python
    Deep Learning-	PyTorch (ResNet-152)
    Database-	MySQL
    GUI-	Tkinter
    ML Utilities-	torchvision, numpy, matplotlib
    Messaging-	Twilio (SMS API)

🧩 System Flow:

   - User logs in or signs up via GUI.

   - Uploads a retinal image.

   - The image is processed and classified using the trained ResNet-152 model.

   - The result is updated in the database and shown on the GUI.

   - An SMS notification is sent with the predicted result.
