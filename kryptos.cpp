#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <fstream>
#include <random>

using namespace std;

string K1CT = "EMUFPHZLRFAXYUSDJKZLDKRNSHGNFIVJYQTQUXQBQVYUVLLTREVJYQTMKYRDMFD";
string K1PT = "BETWEENSUBTLESHADINGANDTHEABSENCEOFLIGHTLIESTHENUANCEOFIQLUSION";

string K2CT = "VFPJUDEEHZWETZYVGWHKKQETGFQJNCEGGWHKK?DQMCPFQZDQMMIAGPFXHQRLGTIMVMZJANQLVKQEDAGDVFRPJUNGEUNAQZGZLECGYUXUEENJTBJLBQCRTBJDFHRRYIZETKZEMVDUFKSJHKFWHKUWQLSZFTIHHDDDUVH?DWKBFUFPWNTDFIYCUQZEREEVLDKFEZMOQQJLTTUGSYQPFEUNLAVIDXFLGGTEZ?FKZBSFDQVGOGIPUFXHHDRKFFHQNTGPUAECNUVPDJMQCLQUMUNEDFQELZZVRRGKFFVOEEXBDMVPNFQXEZLGREDNQFMPNZGLFLPMRJQYALMGNUVPDXVKPDQUMEBEDMHDAFMJGZNUPLGESWJLLAETG";
string K2PT = "ITWASTOTALLYINVISIBLEHOWSTHATPOSSIBLE?THEYUSEDTHEEARTHSMAGNETICFIELDXTHEINFORMATIONWASGATHEREDANDTRANSMITTEDUNDERGRUUNDTOANUNKNOWNLOCATIONXDOESLANGLEYKNOWABOUTTHIS?THEYSHOULDITSBURIEDOUTTHERESOMEWHEREXWHOKNOWSTHEEXACTLOCATION?ONLYWWTHISWASHISLASTMESSAGEXTHIRTYEIGHTDEGREESFIFTYSEVENMINUTESSIXPOINTFIVESECONDSNORTHSEVENTYSEVENDEGREESEIGHTMINUTESFORTYFOURSECONDSWESTxLAYERTWO";

string K3CT = "ENDYAHROHNLSRHEOCPTEOIBIDYSHNAIACHTNREYULDSLLSLLNOHSNOSMRWXMNETPRNGATIHNRARPESLNNELEBLPIIACAEWMTWNDITEENRAHCTENEUDRETNHAEOETFOLSEDTIWENHAEIOYTEYQHEENCTAYCREIFTBRSPAMHHEWENATAMATEGYEERLBTEEFOASFIOTUETUAEOTOARMAEERTNRTIBSEDDNIAAHTTMSTEWPIEROAGRIEWFEBAECTDDHILCEIHSITEGOEAOSDDRYDLORITRKLMLEHAGTDHARDPNEOHMGFMFEUHEECDMRIPFEIMEHNLSSTTRTVDOHW?";
string K3PT = "SLOWLYDESPARATLYSLOWLYTHEREMAINSOFPASSAGEDEBRISTHATENCUMBEREDTHELOWERPARTOFTHEDOORWAYWASREMOVEDWITHTREMBLINGHANDSIMADEATINYBREACHINTHEUPPERLEFTHANDCORNERANDTHENWIDENINGTHEHOLEALITTLEIINSERTEDTHECANDLEANDPEEREDINTHEHOTAIRESCAPINGFROMTHECHAMBERCAUSEDTHEFLAMETOFLICKERBUTPRESENTLYDETAILSOFTHEROOMWITHINEMERGEDFROMTHEMISTXCANYOUSEEANYTHINGQ?";

string K4CT = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR";
string K4CR = "?????????????????????EASTNORTHEAST?????????????????????????????BERLINCLOCK???????????????????????";
string K4CL = "EASTNORTHEASTBERLINCLOCK";

string ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
double ENG_FREQS[26] = {0.081238378, 0.014892788, 0.027114200, 0.043191829, 0.120195499,
                        0.023038568, 0.020257483, 0.059214604, 0.073054201, 0.001031250,
                        0.006895114, 0.039785412, 0.026115862, 0.069477738, 0.076811682,
                        0.018189498, 0.001124502, 0.060212942, 0.062807524, 0.090985886,
                        0.028776268, 0.011074969, 0.020948640, 0.001727893, 0.021135143,
                        0.000702128};

string GenAlphabet(string _Key)
{
    string generated;

    for (int i = 0; i < _Key.length(); ++i)
    {
        if (generated.find(_Key[i]) == string::npos)
        {
            generated += _Key[i];
        }
    }
    for (int i = 0; i < ALPHABET.length(); ++i)
    {
        if (generated.find(ALPHABET[i]) == string::npos)
        {
            generated += ALPHABET[i];
        }
    }

    return generated;
}

string EncryptVigenere(const string &_Text, const string &_Alphabet, const string &_Key)
{
    string ct;
    size_t keyLength = _Key.length();
    size_t skipped = 0;
    vector<int> offsets;

    for (size_t i = 0; i < keyLength; ++i)
    {
        offsets.push_back(_Alphabet.find(_Key[i]));
    }

    for (size_t i = 0; i < _Text.length(); ++i)
    {
        char c = _Text[i];

        size_t p = _Alphabet.find(c);
        if (p == string::npos)
        {
            ct += c;
            ++skipped;
            continue;
        }
        else
        {
            p = (p + 26 + offsets[(i - skipped) % keyLength]) % 26;
            ct += _Alphabet[p];
        }
    }

    return ct;
}

string DecryptVigenere(const string &_Text, const string &_Alphabet, const string &_Key)
{
    string pt;
    size_t keyLength = _Key.length();
    size_t skipped = 0;
    vector<int> offsets;

    for (size_t i = 0; i < keyLength; ++i)
    {
        offsets.push_back(_Alphabet.find(_Key[i]));
    }

    for (size_t i = 0; i < _Text.length(); ++i)
    {
        char c = _Text[i];

        size_t p = _Alphabet.find(c);
        if (p == string::npos)
        {
            pt += c;
            ++skipped;
            continue;
        }
        else
        {
            p = (p + 26 - offsets[(i - skipped) % keyLength]) % 26;
            pt += _Alphabet[p];
        }
    }

    return pt;
}

vector<double> Histogram(const string &_Text)
{
    vector<double> histogram;
    histogram.resize(26);
    size_t count = 0;

    for (int i = 0; i < _Text.length(); ++i)
    {
        if (ALPHABET.find(_Text[i]) != string::npos)
        {
            histogram[_Text[i] - 'A'] += 1.0;
            ++count;
        }
    }

    for (int i = 0; i < 26; ++i)
    {
        histogram[i] = histogram[i] / count;
    }

    return histogram;
}

double VarianceFromEnglish(const string &_Text)
{
    vector<double> histogram = Histogram(_Text);
    double variance = 0.0;

    for (int i = 0; i < 26; ++i)
    {
        double d = histogram[i] - ENG_FREQS[i];
        variance += d * d;
    }

    return variance;
}

string RotateCW(const string &_Text, int _NbCols)
{
    string padded = _Text;

    while (padded.length() % _NbCols != 0)
    {
        padded.push_back('?');
    }

    size_t W = _NbCols;
    size_t H = padded.length() / W;

    string transposed;

    for (int x = 0; x < W; ++x)
    {
        for (int y = H - 1; y > -1; --y)
        {
            transposed += padded[y * W + x];
        }
    }

    return transposed;
}

string RotateCCW(const string &_Text, int _NbCols)
{
    string padded = _Text;

    while (padded.length() % _NbCols != 0)
    {
        padded.push_back('?');
    }

    size_t W = _NbCols;
    size_t H = padded.length() / W;

    string transposed;

    for (int x = W - 1; x > -1; --x)
    {
        for (int y = 0; y < H; ++y)
        {
            transposed += padded[y * W + x];
        }
    }

    return transposed;
}

bool HasCribLetters(const string &_Text, const string &_Crib)
{
    vector<size_t> positions;
    size_t textLength = _Text.length();

    for (int i = 0; i < _Crib.length(); ++i)
    {
        char c = _Crib[i];
        bool found = false;
        for (int j = 0; j < textLength; ++j)
        {
            if (_Text[j] == c && find(positions.begin(), positions.end(), j) == positions.end())
            {
                positions.push_back(j);
                found = true;
                break;
            }
        }
        if (!found)
        {
            return false;
        }
    }

    return true;
}

string SwizzleENDYAHR(const string &_Text)
{
    string left;
    string right;
    for (int i = 0; i < _Text.length(); ++i)
    {
        if ((i % 7 == 0) || (i % 7 == 1) || (i % 7 == 2) || (i % 7 == 5))
        {
            left += _Text[i];
        }
        else
        {
            right += _Text[i];
        }
    }
    return left + right;
}

string SwizzleENDYAHR_2(const string &_Text)
{
    string swizzled;
    string left, right;
    for (int i = 0; i < _Text.length(); ++i)
    {
        if (i % 7 == 0)
        {
            swizzled += left;
            swizzled += right;
            left.clear();
            right.clear();
        }
        if ((i % 7 == 0) || (i % 7 == 1) || (i % 7 == 2) || (i % 7 == 5))
        {
            left += _Text[i];
        }
        else
        {
            right += _Text[i];
        }
    }
    return swizzled;
}

string BlockRotate(const string &_Text)
{
    string left = "?" + _Text.substr(0, 48);
    string right = _Text.substr(48);

    return RotateCW(left, 7) + RotateCCW(right, 7);
}

string Randomise(const string &_Text)
{
    string random;
    vector<char> letters;

    for (int i = 0; i < _Text.length(); ++i)
    {
        letters.push_back(_Text[i]);
    }

    while (letters.size() > 0)
    {
        int pos = (int)(((float)rand() / (float)RAND_MAX) * (letters.size() - 1));
        random += letters[pos];
        letters.erase(letters.begin() + pos);
    }
    return random;
}

string Shift(const string &_Text, int offset)
{
    string shifted;
    offset = (offset + _Text.length()) % _Text.length();
    for (int i = offset; i < _Text.length(); ++i)
    {
        shifted += _Text[i];
    }
    for (int i = 0; shifted.length() < _Text.length(); ++i)
    {
        shifted += _Text[i];
    }
    return shifted;
}

bool isAlpha(const string &_Text)
{
    auto it = find_if(_Text.begin(), _Text.end(), [](char const &c)
                      { return !isalpha(c); });

    return it == _Text.end();
}

string toUpper(const string &_Text)
{
    string up;
    for (int i = 0; i < _Text.length(); ++i)
    {

        up += toupper(_Text[i]);
    }
    return up;
}

string makeAlpha(const string &_Text)
{
    string alpha;
    for (int i = 0; i < _Text.length(); ++i)
    {
        if (isalpha(_Text[i]))
        {
            alpha += _Text[i];
        }
    }
    return alpha;
}

void RunTests()
{
    string kAlphabet = GenAlphabet("KRYPTOS");
    printf("%s\n", kAlphabet.c_str());

    printf("K1 PT: %s\n", K1PT.c_str());
    printf("K1 EN: %s\n", EncryptVigenere(K1PT, kAlphabet, "PALIMPSEST").c_str());
    printf("K1 CT: %s\n", K1CT.c_str());

    printf("K2 CT: %s\n", K2CT.c_str());
    printf("K2 DE: %s\n", DecryptVigenere(K2CT, kAlphabet, "ABSCISSA").c_str());
    printf("K2 PT: %s\n", K2PT.c_str());

    printf("K3CT variance: %f\n", VarianceFromEnglish(K3CT));
    printf("K4CR variance: %f\n", VarianceFromEnglish(K4CR));

    printf("CW:  %s\n", RotateCW("ABCDABCDABC", 4).c_str());
    printf("CCW: %s\n", RotateCCW("ABCDABCDABC", 4).c_str());

    printf("%i\n", HasCribLetters("ABCDEABCDE", "BCBE"));
    printf("%i\n", HasCribLetters("ABCDEABCDE", "BCBEX"));

    printf("%s\n", Shift("0123456789", 3).c_str());
    printf("%s\n", Shift("0123456789", -3).c_str());
}

struct Match
{
    string keyword;
    string pt;
    double variance;
};

void Attempt_RotateAndDecrypt()
{
    string kAlphabet = GenAlphabet("KRYPTOS");

    for (int r = 2; r < 49; ++r)
    {
        string ct = makeAlpha(RotateCW(K4CT, r));
        reverse(ct.begin(), ct.end());

        printf("%i\t%s\n", r, ct.c_str());

        vector<Match> matches;
        ifstream file("Words.txt");
        string word;
        while (getline(file, word))
        {
            word = toUpper(word);
            if (!isAlpha(word))
            {
                continue;
            }

            string pt = DecryptVigenere(ct, kAlphabet, word);
            if (HasCribLetters(pt, K4CL))
            {
                Match m;
                m.keyword = word;
                m.pt = pt;
                m.variance = VarianceFromEnglish(pt);
                matches.push_back(m);
            }
        }

        sort(matches.begin(), matches.end(), [](const Match &a, const Match &b)
             { return a.variance < b.variance; });

        printf("%s\t%f\n", matches[0].keyword.c_str(), matches[0].variance);
        printf("%s\n", matches[0].pt.c_str());
        printf("%s\n\n", K4CR.c_str());
    }
}

void Attempt_ShiftAndDecrypt()
{
    // Try all shifts ok K4 and then decrypt to see if one of the crib words appears
    //  
    // Outcome: Nothing interesting came out of it

    string kAlphabet = GenAlphabet("KRYPTOS");

    for (int off = 0; off < K4CT.length(); ++off)
    {
        string ct = Shift(K4CT, off);
        printf("%s\n", ct.c_str());

        vector<Match> matches;
        ifstream file("Words.txt");
        string word;
        while (getline(file, word))
        {
            word = toUpper(makeAlpha(word));
            if (word.length() == 0)
            {
                continue;
            }

            string pt = DecryptVigenere(ct, kAlphabet, word);
            if (HasCribLetters(pt, K4CL) && (pt.find("CLOCK") != string::npos))
            {
                Match m;
                m.keyword = word;
                m.pt = pt;
                m.variance = VarianceFromEnglish(pt);
                matches.push_back(m);
            }
        }

        sort(matches.begin(), matches.end(), [](const Match &a, const Match &b)
             { return a.variance < b.variance; });

        for (int i = 0; i < matches.size(); ++i)
        {
            printf("%s\t%f\t%s\n", matches[i].keyword.c_str(), matches[i].variance, matches[i].pt.c_str());
        }
    }
}

int main()
{
    RunTests();
    
    // Attempt_RotateAndDecrypt();
    Attempt_ShiftAndDecrypt();

    return 0;
}
