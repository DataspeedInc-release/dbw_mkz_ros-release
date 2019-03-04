/*********************************************************************
 * C++ unit test for dbw_mkz_can/PlatformVersion.h
 *********************************************************************/

#include <gtest/gtest.h>

// File under test
#include <dbw_mkz_can/PlatformVersion.h>
using namespace dbw_mkz_can;

// Test empty constructor
TEST(PlatformVersion, empty)
{
  EXPECT_EQ((Platform)0,     PlatformVersion().p);
  EXPECT_EQ(  (Module)0,     PlatformVersion().m);
  EXPECT_EQ(ModuleVersion(), PlatformVersion().v);
}

// Test that fields are populated by each constructor
TEST(PlatformVersion, constructor)
{
  EXPECT_EQ((Platform)1,          PlatformVersion((Platform)1, (Module)2, ModuleVersion(3,4,5)).p);
  EXPECT_EQ((Module)2,            PlatformVersion((Platform)1, (Module)2, ModuleVersion(3,4,5)).m);
  EXPECT_EQ(ModuleVersion(3,4,5), PlatformVersion((Platform)1, (Module)2, ModuleVersion(3,4,5)).v);
  EXPECT_EQ((Platform)1,          PlatformVersion((Platform)1, (Module)2, 3, 4, 5).p);
  EXPECT_EQ((Module)2,            PlatformVersion((Platform)1, (Module)2, 3, 4, 5).m);
  EXPECT_EQ(ModuleVersion(3,4,5), PlatformVersion((Platform)1, (Module)2, 3, 4, 5).v);
}

// Test operators
TEST(ModuleVersion, operators)
{
  const Platform x = (Platform)1; const Module y = (Module)2;
  const Platform X = (Platform)3; const Module Y = (Module)3;

  // Compare PlatformVersion with PlatformVersion
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) <  PlatformVersion(x,y,1,1,1));
  EXPECT_TRUE (PlatformVersion(x,y,1,1,1) <  PlatformVersion(x,y,9,9,9));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) <  PlatformVersion(X,y,9,9,9));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) <  PlatformVersion(x,Y,9,9,9));
  EXPECT_FALSE(PlatformVersion(x,y,9,9,9) <= PlatformVersion(x,y,1,1,1));
  EXPECT_TRUE (PlatformVersion(x,y,1,1,1) <= PlatformVersion(x,y,1,1,1));
  EXPECT_TRUE (PlatformVersion(x,y,1,1,1) <= PlatformVersion(x,y,9,9,9));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) <= PlatformVersion(X,y,9,9,9));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) <= PlatformVersion(x,Y,9,9,9));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) >  PlatformVersion(x,y,9,9,9));
  EXPECT_TRUE (PlatformVersion(x,y,9,9,9) >  PlatformVersion(x,y,1,1,1));
  EXPECT_FALSE(PlatformVersion(x,y,9,9,9) >  PlatformVersion(X,y,1,1,1));
  EXPECT_FALSE(PlatformVersion(x,y,9,9,9) >  PlatformVersion(x,Y,1,1,1));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) >= PlatformVersion(x,y,9,9,9));
  EXPECT_TRUE (PlatformVersion(x,y,1,1,1) >= PlatformVersion(x,y,1,1,1));
  EXPECT_TRUE (PlatformVersion(x,y,9,9,9) >= PlatformVersion(x,y,1,1,1));
  EXPECT_FALSE(PlatformVersion(x,y,9,9,9) >= PlatformVersion(X,y,1,1,1));
  EXPECT_FALSE(PlatformVersion(x,y,9,9,9) >= PlatformVersion(x,Y,1,1,1));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) == PlatformVersion(x,y,9,9,9));
  EXPECT_TRUE (PlatformVersion(x,y,1,1,1) == PlatformVersion(x,y,1,1,1));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) == PlatformVersion(X,y,1,1,1));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) == PlatformVersion(x,Y,1,1,1));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) != PlatformVersion(x,y,1,1,1));
  EXPECT_TRUE (PlatformVersion(x,y,1,1,1) != PlatformVersion(x,y,9,9,9));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) != PlatformVersion(X,y,9,9,9));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) != PlatformVersion(x,Y,9,9,9));

  // Compare PlatformVersion with ModuleVersion
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) <  ModuleVersion(1,1,1));
  EXPECT_TRUE (PlatformVersion(x,y,1,1,1) <  ModuleVersion(9,9,9));
  EXPECT_FALSE(PlatformVersion(x,y,9,9,9) <= ModuleVersion(1,1,1));
  EXPECT_TRUE (PlatformVersion(x,y,1,1,1) <= ModuleVersion(1,1,1));
  EXPECT_TRUE (PlatformVersion(x,y,1,1,1) <= ModuleVersion(9,9,9));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) >  ModuleVersion(9,9,9));
  EXPECT_TRUE (PlatformVersion(x,y,9,9,9) >  ModuleVersion(1,1,1));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) >= ModuleVersion(9,9,9));
  EXPECT_TRUE (PlatformVersion(x,y,1,1,1) >= ModuleVersion(1,1,1));
  EXPECT_TRUE (PlatformVersion(x,y,9,9,9) >= ModuleVersion(1,1,1));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) == ModuleVersion(9,9,9));
  EXPECT_TRUE (PlatformVersion(x,y,1,1,1) == ModuleVersion(1,1,1));
  EXPECT_FALSE(PlatformVersion(x,y,1,1,1) != ModuleVersion(1,1,1));
  EXPECT_TRUE (PlatformVersion(x,y,1,1,1) != ModuleVersion(9,9,9));
}

int main(int argc, char **argv)
{
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

