#ifndef __HiJetAlgos_UEParameters_h__
#define __HiJetAlgos_UEParameters_h__


class UEParameters {
 public:
  UEParameters(std::vector<float> *v = 0, int nn = 1, int neta = 1){
    rawParameters_ = v;
    nn_ = nn;

  }

  get_vn(int n, int eta){
    int offset = 0;
    int index = 0;
    return rawParameters_[index];
  }

 private:
  std::vector<float> *rawParameters_;
  int nn_;
  int neta_;

};


#endif
