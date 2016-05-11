#include <iostream>

namespace Simple {

    /*! @brief Does something
     *
     * In detail the Whatever class still doesn't do anything useful
     *
     * \tparam T1 fulfills the concept of a type
     */

    template <typename T1>
    class Whatever {
    public:
      //! public typedef
      typedef MyInt int;

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