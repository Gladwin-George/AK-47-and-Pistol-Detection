![Copy of banner](https://user-images.githubusercontent.com/76112629/235502400-0018d5c7-5530-4173-830a-bd07c0443322.png)


# AK 47 and Pistol Detection

In todays world, Weapons like pistol and AK 47 are one of the common weapons used in crimes. It is not possible to ban people from using them so best way to decrease crime caused due to using these weapons is to detect them as soon as spotted and take necesary actions.

This detection system aims to solve this issue. This system can detect weapons like AK47 and Pistol. Identifying weapons type can help in determinig how big the incident can be and how much action should be taken. There are many kinds and variety of weapons but this syatem detects only two kinds as this are the common weapons used in crimes.  

## Dataset

The dataset contain images of AK47 and pistol in different scenarios and pangles so that the system can detect them in as many as different situations as possible. As their are many ways guns can be hold.

## Model Training

The model to detect the guns are trained using YOLOv8. Ultralytics YOLOv8 is a cutting-edge, state-of-the-art (SOTA) model that builds upon the success of previous YOLO versions and introduces new features and improvements to further boost performance and flexibility. 

## Model Detection Results

### Input:
<p align="center">
    <img src="https://user-images.githubusercontent.com/76112629/235494442-8482f0e4-f345-4a92-900c-68391e0de306.jpg" alt="Image 1" width="300" height="200" hspace="20">
    <img src="https://user-images.githubusercontent.com/76112629/235497816-b9c7dfc4-3e51-4831-93ef-e3d9091a806f.jpg" alt="Image 2" width="300" height="200" hspace="20">
</p>


### Output:

<p align="center">
    <img src="https://user-images.githubusercontent.com/76112629/235494358-3096a325-061d-4d0e-86fc-62971519b9f1.jpg" alt="Image 1" width="300" height="200" hspace="20">
    <img src="https://user-images.githubusercontent.com/76112629/235498052-c22597b7-6081-491e-83d3-6bf76a0e82e3.jpg" alt="Image 2" width="300" height="200" hspace="20">


