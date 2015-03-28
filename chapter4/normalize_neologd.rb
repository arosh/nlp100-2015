# https://github.com/neologd/mecab-ipadic-neologd/wiki/Regexp.ja
require 'moji'

def normalize_neologd(norm)
  norm.tr!("０-９Ａ-Ｚａ-ｚ", "0-9A-Za-z")
  norm = Moji.han_to_zen(norm, Moji::HAN_KATA)
  hypon_reg = /(?:˗|֊|‐|‑|‒|–|⁃|⁻|₋|−)/
  norm.gsub!(hypon_reg, "-")
  choon_reg = /(?:﹣|－|ｰ|—|―|─|━)/
  norm.gsub!(choon_reg, "ー")
  chil_reg = /(?:~|∼|∾|〜|〰|～)/
  norm.gsub!(chil_reg, '')
  norm.gsub!(/[ー]+/, "ー")
  norm.tr!(%q{!"#$%&'()*+,-.\/:;<=>?@[\]^_`{|}~｡､･｢｣"}, %q{！”＃＄％＆’（）＊＋，−．／：；＜＝＞？＠［￥］＾＿｀｛｜｝〜。、・「」})
  norm.gsub!(/　/, " ")
  norm.gsub!(/ {1,}/, " ")
  norm.gsub!(/^[ ]+(.+?)$/, "\\1")
  norm.gsub!(/^(.+?)[ ]+$/, "\\1")
  while norm =~ %r{([\p{InCJKUnifiedIdeographs}\p{InHiragana}\p{InKatakana}\p{InHalfwidthAndFullwidthForms}\p{InCJKSymbolsAndPunctuation}]+)[ ]{1}([\p{InCJKUnifiedIdeographs}\p{InHiragana}\p{InKatakana}\p{InHalfwidthAndFullwidthForms}\p{InCJKSymbolsAndPunctuation}]+)}
    norm.gsub!( %r{([\p{InCJKUnifiedIdeographs}\p{InHiragana}\p{InKatakana}\p{InHalfwidthAndFullwidthForms}\p{InCJKSymbolsAndPunctuation}]+)[ ]{1}([\p{InCJKUnifiedIdeographs}\p{InHiragana}\p{InKatakana}\p{InHalfwidthAndFullwidthForms}\p{InCJKSymbolsAndPunctuation}]+)}, "\\1\\2")
  end
  while norm =~ %r{([\p{InBasicLatin}]+)[ ]{1}([\p{InCJKUnifiedIdeographs}\p{InHiragana}\p{InKatakana}\p{InHalfwidthAndFullwidthForms}\p{InCJKSymbolsAndPunctuation}]+)}
    norm.gsub!(%r{([\p{InBasicLatin}]+)[ ]{1}([\p{InCJKUnifiedIdeographs}\p{InHiragana}\p{InKatakana}\p{InHalfwidthAndFullwidthForms}\p{InCJKSymbolsAndPunctuation}]+)}, "\\1\\2")
  end
  while norm =~ %r{([\p{InCJKUnifiedIdeographs}\p{InHiragana}\p{InKatakana}\p{InHalfwidthAndFullwidthForms}\p{InCJKSymbolsAndPunctuation}]+)[ ]{1}([\p{InBasicLatin}]+)}
    norm.gsub!(%r{([\p{InCJKUnifiedIdeographs}\p{InHiragana}\p{InKatakana}\p{InHalfwidthAndFullwidthForms}\p{InCJKSymbolsAndPunctuation}]+)[ ]{1}([\p{InBasicLatin}]+)}, "\\1\\2")
  end
  norm.tr!(
    %q{！”＃＄％＆’（）＊＋，−．／：；＜＞？＠［￥］＾＿｀｛｜｝〜},
    %q{!"#$%&'()*+,-.\/:;<>?@[\]^_`{|}~}
  )
  norm
end

if $0 == __FILE__
  ARGF.each do |line|
    puts normalize_neologd(line)
  end
end
