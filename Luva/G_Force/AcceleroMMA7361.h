#ifndef AcceleroMMA7361_h
#define AcceleroMMA7361_h

#if defined(ARDUINO) && ARDUINO >= 100
#include <Arduino.h>
#else
#include <WProgram.h>
#include <pins_arduino.h>
#endif

class AcceleroMMA7361
{
  public:
    AcceleroMMA7361();
    void begin();
    void begin(int sleepPin, int selfTestPin, int zeroGPin, int gSelectPin, int xPin, int yPin, int zPin);
    int getXRaw();
    int getYRaw();
    int getZRaw();
    int getXVolt();
    int getYVolt();
    int getZVolt();
    int getXAccel();
    int getYAccel();
    int getZAccel();
    void getAccelXYZ(int *_XAxis, int *_YAxis, int *_ZAxis);
    int getTotalVector();
    void setOffSets(int xOffSet, int yOffSet, int zOffSet);
    void calibrate();                             // only to be executed when Z-axis is oriented to the ground
// it calculates the offset values by assuming  Z = +1 G ; X and Y  = 0 G
    void setARefVoltage(double _refV);
    void setAveraging(int avg);
    int getOrientation();
    void setSensitivity(boolean sensi);
    void sleep();
    void wake();

  private:
    int _mapMMA7361V(int value);
    int _mapMMA7361G(int value);
    int _sleepPin;
    int _selfTestPin;
    int _zeroGPin;
    int _gSelectPin;
    int _xPin;
    int _yPin;
    int _zPin;
    int _polarities[3];
    double _refVoltage;
    boolean _sleep;
    boolean _sensi;
   public:
    int offSets[3];
    int average;
};
#endif
