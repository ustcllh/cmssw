#ifndef __HiJetAlgos_UEParameters_h__
#define __HiJetAlgos_UEParameters_h__

#include <boost/multi_array.hpp>

class UEParameters {
private:
	static const size_t nreduced_particle_flow_id = 3;
	const std::vector<float> *v_;
	int nn_;
	int neta_;
	boost::const_multi_array_ref<float, 4> *parameters_;
public:
	UEParameters(const std::vector<float> *v = 0, int nn = 1, int neta = 1)
		: v_(v), nn_(nn), neta_(neta)
	{
		parameters_ = new boost::const_multi_array_ref<float, 4>(&(*v)[0], boost::extents[neta][nreduced_particle_flow_id][nn][2]);
	}
	const std::vector<float> get_raw(void) const
	{
		return *v_;
	}
	void get_fourier(double &re, double &im, size_t n, size_t eta) const
	{
		re = 0;
		im = 0;
		for (size_t i = 0; i < nreduced_particle_flow_id; i++) {
			re += (*parameters_)[eta][i][n][0];
			im += (*parameters_)[eta][i][n][1];
		}
	}
	~UEParameters(void)
	{
		delete parameters_;
	}
	double get_sum_pt(int eta) const
	{
		double re;
		double im;

		get_fourier(re, im, 0, eta);

		// There is no imaginary part
		return re;
	}
	double get_vn(int n, int eta) const
	{
		if (n < 0) {
			return NAN;
		}
		else if (n == 0) {
			return 1;
		}

		double re;
		double im;

		get_fourier(re, im, n, eta);

		return sqrt(re * re + im * im) / get_sum_pt(eta);
	}
	double get_psin(int n, int eta) const
	{
		if (n <= 0) {
			return 0;
		}

		double re;
		double im;

		get_fourier(re, im, n, eta);

		return atan2(im, re) / n;
	}
};

#endif
