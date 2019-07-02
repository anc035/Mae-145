import numpy as np
import sys,os
from PIL import Image
import matplotlib.pyplot as plt


def intersection_over_union(prediction, ground_truth):
    """
    Compute the IOU between a predicted segmentation and a ground-truth
    :param prediction: A (height, width) boolean array indicating the predicted segmentation
    :param ground_truth: A (height, width) boolean array indicating the correct segmentation
    :return float: The IOU score
    """
    return np.sum(prediction & ground_truth, dtype=float) / np.sum(prediction | ground_truth)


def blue_region_segmenter(rgb_image, relative_blueness_threshold = 1.):
    """
    Segment out the blue regions of the image.
    :param rgb_image: A (height, width, 3) RGB image numpy array
    :param relative_blueness_threshold: The threshold for how strong the blue should be relative to the red+green
    :return: A (height, width) boolean numpy array indicating the pixels occupied by the bin
    """
    labels = rgb_image[:, :, 2] > relative_blueness_threshold * (rgb_image[:, :, 0].astype(float) + rgb_image[:, :, 1])
    return labels


def bluest_rectangle_segmenter(rgb_image, rectangle_size=(120, 80)):
    """
    Segment out the bluest rectangle of the given size in the image.
    :param rgb_image: A (height, width, 3) RGB image numpy array
    :param rectangle_size: The (rect_height, rect_width) of the rectangle which you expect the bin to occupy
    :return: A (height, width) boolean numpy array indicating the pixels occupied by the bin
    """
    ry, rx = rectangle_size
    relative_blueness = rgb_image[:, :, 2].astype(float)/(rgb_image.astype(float).sum(axis=2)+1e-6)
    integral_image = relative_blueness.cumsum(axis=0).cumsum(axis=1)
    blueness_in_box = integral_image[ry:, rx:] - integral_image[:-ry, rx:] - integral_image[ry:, :-rx] + integral_image[:-ry, :-rx]
    row, col = np.unravel_index(blueness_in_box.argmax(), blueness_in_box.shape)
    labels = np.zeros(relative_blueness.shape, dtype=np.bool)
    labels[row:row+ry, col:col+rx] = True
    return labels

def load_images(argv):
    """
    Takes in path and loads images and labels in numerical order.
    :param argv: A string of path/to/data folder
    :return: A list of (height, width, 3) RGB image numpy arrays,
             A list of (height, width) boolean numpy arrays indicating the correct segmentation
    """
    
    images=[]
    labels=[]
    try:
        path=sys.argv[1]
        print ("Data Directory:", path)
        for filename in sorted(os.listdir(path)):
            if filename.startswith('image'):
                with Image.open(os.path.join(path,filename)) as image:
                    images.append(np.asarray(image))
            if filename.startswith('label'):
                with Image.open(os.path.join(path,filename)) as label:
                    labels.append(np.asarray(label,dtype=bool))
    except:
        print("ERROR:Input path/to/data")
        sys.exit(1)

    return images,labels

def determine_best_parameters(images,labels,intersection_over_union):
    """
    Determines best paramter values for each segmenter.
    :param images A (height,width,3) RGB image numpy array,
    :param labels A (height,width) boolean numpy array indicating correct segmentation
    :function intersection_over_union computes IOU score
    return  best_region_param float that gives best IOU score for blue_region_segmenter
            best_rectangle_param (height,width) tuple that gives best IOU score for bluest_rectangle_segmenter

    """
    #generate range of param values to determine best value
    N=20
    rectangle_height=np.linspace(30,200,N,dtype=int)
    rectangle_width=np.linspace(20,130,N,dtype=int)

    rectangle_range=(tuple(zip(rectangle_height,rectangle_width)))
    relative_blueness_threshold_range=np.linspace(0.1,2.0, num=N)

    best_region_score=0
    best_rectangle_score=0
    best_region_param=0
    best_rectangle_param=0

    #Calculate average IOU score per segmenter per param value
    for region_param, rectangle_param in zip(relative_blueness_threshold_range,rectangle_range):
        blue_region_prediction,bluest_rectangle_prediction=generate_predictions(images,region_param,rectangle_param)
        blue_region_scores,bluest_rectangle_scores=generate_scores(labels,blue_region_prediction,bluest_rectangle_prediction)
        average_region_score=np.average(blue_region_scores)
        average_rectangle_score=np.average(bluest_rectangle_scores)

        if average_region_score> best_region_score:
            best_region_score=average_region_score
            best_region_param=region_param
        if average_rectangle_score >best_rectangle_score:
            best_rectangle_score=average_rectangle_score
            best_rectangle_param=rectangle_param
    print('Best Blue Region Parameter {:.2f}'.format(best_region_param))
    print('Best Blue Rectangle Parameter',best_rectangle_param)
    print('        {}   {}'.format('blue_region_scores','bluest_rectangle_scores'))
    print('Average Score{:8.2f} {:20.2f} \n'.format(best_region_score,best_rectangle_score))
    
    return best_region_param, best_rectangle_param
                    

def generate_predictions(images,region_param,rectangle_param):
    """
    Generates predictions of blue bin location per segmenter
    :param images A (height,width,3) RGB image numpy array,
    :param region_param A float value for relative_blueness_threshold
    :param rectangle_param A (height,width) tuple indicating blue rectangle size
    return blue_region_prediction A list of (height,width) numpy boolean arrays indicating location of bin
           blue_rectangle_prediction A list of (height,width) numpy boolean arrays indicating location of bin
    """
    blue_region_prediction=[]
    bluest_rectangle_prediction=[]
    
    for image in images:
        blue_region_prediction.append(blue_region_segmenter(image,region_param))
        bluest_rectangle_prediction.append(bluest_rectangle_segmenter(image,rectangle_param))
    return blue_region_prediction,bluest_rectangle_prediction

def generate_scores(labels,blue_region_prediction,bluest_rectangle_prediction):
    """
    Generates IOU scores per segmenter 
    :param labels list of (height,width) boolean array indicating correct blue bin pixels
    :param blue_region_prediction list of (height,width) boolean array indicating predicted pixels
    :param bluest_rectangle_prediction list of (height,width) boolean array indicating predicted pixels
    return blue_region_scores list of floats indicating IOU score
           blue_rectangle_scores list of floats indicating IOU score
    """
    blue_region_scores=[]
    bluest_rectangle_scores=[]
    for region_prediction,rectangle_prediction,label in zip(blue_region_prediction,bluest_rectangle_prediction,labels):
        blue_region_scores.append(intersection_over_union(region_prediction,label))
        bluest_rectangle_scores.append(intersection_over_union(rectangle_prediction,label))
    
    return blue_region_scores, bluest_rectangle_scores


if __name__=="__main__":
    images,labels=load_images(sys.argv)
    best_region_param, best_rectangle_param=determine_best_parameters(images,labels,intersection_over_union)

    blue_region_prediction,bluest_rectangle_prediction=generate_predictions(images,best_region_param,best_rectangle_param)
    blue_region_scores,bluest_rectangle_scores=generate_scores(labels,blue_region_prediction,bluest_rectangle_prediction)

    #print IOU scores per image
    for index, score in enumerate(zip(blue_region_scores,bluest_rectangle_scores)):
        print('Image #{:<9} {:.2f} {:20.2f}'.format(index,score[0],score[1]))

    images_to_compare=map(int,input('Select Images to Compare: ').split(','))

    #plot predictions and overlay ground truth
    for index in images_to_compare:
        fig=plt.figure(index)
        fig.suptitle('Segmenter Comparison of Image %i'%index)
        plot1=plt.subplot(221)
        plot1.set_title('Blue Region Prediction')
        plt.imshow(blue_region_prediction[index],'Blues')

        plot2=plt.subplot(222)
        plot2.set_title('Bluest Rectangle Prediction')
        plt.imshow(bluest_rectangle_prediction[index],'Blues')

        plot3=plt.subplot(223)
        plot3.set_title('IOU Score: %1.3f'%blue_region_scores[index])
        plt.imshow(blue_region_prediction[index],'Reds',alpha =1.0,interpolation='none')
        plt.imshow(labels[index],'Greens',alpha = 0.8,interpolation='none')
        
        plot4=plt.subplot(224)
        plot4.set_title('IOU Score: %1.3f'%bluest_rectangle_scores[index])
        plt.imshow(bluest_rectangle_prediction[index],'Reds',alpha =1.0,interpolation='none')
        plt.imshow(labels[index],'Greens',alpha = 0.8,interpolation='none')

    plt.show()


