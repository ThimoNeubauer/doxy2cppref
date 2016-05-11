#include <iostream>

namespace Simple {

    class Whatever {
    public:
      //! the trivial constructor
      Whatever();

      //! different constructor
      Whatever(float f);

      //! visible method
      float visible(std::string s);

    private:
      //! a hidden private method
      int hidden() const;

      //! member documentation
      int member;
    };

};