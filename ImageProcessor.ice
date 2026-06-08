module DistributedPhotoProcessor
{
    sequence<byte> ImageData;

    exception InvalidImageException
    {
        string reason;
    };

    interface ImageProcessor
    {
        ImageData Color2BW(ImageData inputImage) throws InvalidImageException;

        ImageData Resize(ImageData inputImage, int width, int height)
            throws InvalidImageException;

        ImageData Rotate(ImageData inputImage, int degrees)
            throws InvalidImageException;

        string Ping();
    };
};